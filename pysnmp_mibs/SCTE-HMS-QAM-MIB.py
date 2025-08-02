_e='qamMpegDocsisCommonGroup'
_d='qamConfigGroup'
_c='qamChannelGroup'
_b='qamConfigOutputProgNoMax'
_a='qamConfigOutputProgNoMin'
_Z='qamConfigUdpPortRangeMax'
_Y='qamConfigUdpPortRangeMin'
_X='qamConfigIPAddr'
_W='qamConfigIPAddrType'
_V='qamConfigQamChannelIdMax'
_U='qamConfigQamChannelIdMin'
_T='qamChannelAnnexMode'
_S='qamChannelContWaveMode'
_R='qamChannelSquelch'
_Q='qamChannelPower'
_P='qamChannelInterleaverMode'
_O='qamChannelInterleaverLevel'
_N='qamChannelModulationFormat'
_M='qamChannelFrequency'
_L='qamChannelCommonUtilization'
_K='qamChannelCommonOutputBw'
_J='qamConfigIndex'
_I='InetAddressType'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='SCTE-HMS-QAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_I)
QAMChannelInterleaveMode,QAMChannelModulationFormat=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-TC-MIB','QAMChannelInterleaveMode','QAMChannelModulationFormat')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heDigitalQamMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,5,3,1))
if mibBuilder.loadTexts:heDigitalQamMIB.setRevisions(('2008-07-16 03:05','2008-04-18 10:55','2008-02-04 18:50','2007-12-17 11:50','2007-10-03 17:00','2007-10-02 12:00'))
_QamMIBObjects_ObjectIdentity=ObjectIdentity
qamMIBObjects=_QamMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,5,3,1,1))
if mibBuilder.loadTexts:qamMIBObjects.setStatus(_A)
_QamChannelTable_Object=MibTable
qamChannelTable=_QamChannelTable_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1))
if mibBuilder.loadTexts:qamChannelTable.setStatus(_A)
_QamChannelEntry_Object=MibTableRow
qamChannelEntry=_QamChannelEntry_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1))
qamChannelEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qamChannelEntry.setStatus(_A)
_QamChannelFrequency_Type=Unsigned32
_QamChannelFrequency_Object=MibTableColumn
qamChannelFrequency=_QamChannelFrequency_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,1),_QamChannelFrequency_Type())
qamChannelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:qamChannelFrequency.setUnits('Hertz')
_QamChannelModulationFormat_Type=QAMChannelModulationFormat
_QamChannelModulationFormat_Object=MibTableColumn
qamChannelModulationFormat=_QamChannelModulationFormat_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,2),_QamChannelModulationFormat_Type())
qamChannelModulationFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelModulationFormat.setStatus(_A)
class _QamChannelInterleaverLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('level1',1),('level2',2)))
_QamChannelInterleaverLevel_Type.__name__=_D
_QamChannelInterleaverLevel_Object=MibTableColumn
qamChannelInterleaverLevel=_QamChannelInterleaverLevel_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,3),_QamChannelInterleaverLevel_Type())
qamChannelInterleaverLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelInterleaverLevel.setStatus(_A)
_QamChannelInterleaverMode_Type=QAMChannelInterleaveMode
_QamChannelInterleaverMode_Object=MibTableColumn
qamChannelInterleaverMode=_QamChannelInterleaverMode_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,4),_QamChannelInterleaverMode_Type())
qamChannelInterleaverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelInterleaverMode.setStatus(_A)
_QamChannelPower_Type=Integer32
_QamChannelPower_Object=MibTableColumn
qamChannelPower=_QamChannelPower_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,5),_QamChannelPower_Type())
qamChannelPower.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelPower.setStatus(_A)
if mibBuilder.loadTexts:qamChannelPower.setUnits('0.1 dBmV')
class _QamChannelSquelch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unmuted',1),('muted',2)))
_QamChannelSquelch_Type.__name__=_D
_QamChannelSquelch_Object=MibTableColumn
qamChannelSquelch=_QamChannelSquelch_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,6),_QamChannelSquelch_Type())
qamChannelSquelch.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelSquelch.setStatus(_A)
class _QamChannelContWaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cwmOff',1),('cwmOn',2)))
_QamChannelContWaveMode_Type.__name__=_D
_QamChannelContWaveMode_Object=MibTableColumn
qamChannelContWaveMode=_QamChannelContWaveMode_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,7),_QamChannelContWaveMode_Type())
qamChannelContWaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelContWaveMode.setStatus(_A)
class _QamChannelAnnexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('other',2),('annexA',3),('annexB',4),('annexC',5)))
_QamChannelAnnexMode_Type.__name__=_D
_QamChannelAnnexMode_Object=MibTableColumn
qamChannelAnnexMode=_QamChannelAnnexMode_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,1,1,8),_QamChannelAnnexMode_Type())
qamChannelAnnexMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelAnnexMode.setStatus(_A)
_QamChannelCommonTable_Object=MibTable
qamChannelCommonTable=_QamChannelCommonTable_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,2))
if mibBuilder.loadTexts:qamChannelCommonTable.setStatus(_A)
_QamChannelCommonEntry_Object=MibTableRow
qamChannelCommonEntry=_QamChannelCommonEntry_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,2,1))
qamChannelCommonEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qamChannelCommonEntry.setStatus(_A)
_QamChannelCommonOutputBw_Type=Integer32
_QamChannelCommonOutputBw_Object=MibTableColumn
qamChannelCommonOutputBw=_QamChannelCommonOutputBw_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,2,1,1),_QamChannelCommonOutputBw_Type())
qamChannelCommonOutputBw.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelCommonOutputBw.setStatus(_A)
if mibBuilder.loadTexts:qamChannelCommonOutputBw.setUnits('bps')
class _QamChannelCommonUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1000))
_QamChannelCommonUtilization_Type.__name__=_D
_QamChannelCommonUtilization_Object=MibTableColumn
qamChannelCommonUtilization=_QamChannelCommonUtilization_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,2,1,2),_QamChannelCommonUtilization_Type())
qamChannelCommonUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qamChannelCommonUtilization.setStatus(_A)
if mibBuilder.loadTexts:qamChannelCommonUtilization.setUnits('0.1 Percent')
_QamConfigTable_Object=MibTable
qamConfigTable=_QamConfigTable_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3))
if mibBuilder.loadTexts:qamConfigTable.setStatus(_A)
_QamConfigEntry_Object=MibTableRow
qamConfigEntry=_QamConfigEntry_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1))
qamConfigEntry.setIndexNames((0,_G,_H),(0,_B,_J))
if mibBuilder.loadTexts:qamConfigEntry.setStatus(_A)
_QamConfigIndex_Type=Unsigned32
_QamConfigIndex_Object=MibTableColumn
qamConfigIndex=_QamConfigIndex_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,1),_QamConfigIndex_Type())
qamConfigIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qamConfigIndex.setStatus(_A)
class _QamConfigQamChannelIdMin_Type(Integer32):defaultValue=1
_QamConfigQamChannelIdMin_Type.__name__=_D
_QamConfigQamChannelIdMin_Object=MibTableColumn
qamConfigQamChannelIdMin=_QamConfigQamChannelIdMin_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,2),_QamConfigQamChannelIdMin_Type())
qamConfigQamChannelIdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigQamChannelIdMin.setStatus(_A)
_QamConfigQamChannelIdMax_Type=Integer32
_QamConfigQamChannelIdMax_Object=MibTableColumn
qamConfigQamChannelIdMax=_QamConfigQamChannelIdMax_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,3),_QamConfigQamChannelIdMax_Type())
qamConfigQamChannelIdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigQamChannelIdMax.setStatus(_A)
class _QamConfigIPAddrType_Type(InetAddressType):defaultValue=1
_QamConfigIPAddrType_Type.__name__=_I
_QamConfigIPAddrType_Object=MibTableColumn
qamConfigIPAddrType=_QamConfigIPAddrType_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,4),_QamConfigIPAddrType_Type())
qamConfigIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigIPAddrType.setStatus(_A)
_QamConfigIPAddr_Type=InetAddress
_QamConfigIPAddr_Object=MibTableColumn
qamConfigIPAddr=_QamConfigIPAddr_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,5),_QamConfigIPAddr_Type())
qamConfigIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigIPAddr.setStatus(_A)
class _QamConfigUdpPortRangeMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QamConfigUdpPortRangeMin_Type.__name__=_D
_QamConfigUdpPortRangeMin_Object=MibTableColumn
qamConfigUdpPortRangeMin=_QamConfigUdpPortRangeMin_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,6),_QamConfigUdpPortRangeMin_Type())
qamConfigUdpPortRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigUdpPortRangeMin.setStatus(_A)
class _QamConfigUdpPortRangeMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QamConfigUdpPortRangeMax_Type.__name__=_D
_QamConfigUdpPortRangeMax_Object=MibTableColumn
qamConfigUdpPortRangeMax=_QamConfigUdpPortRangeMax_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,7),_QamConfigUdpPortRangeMax_Type())
qamConfigUdpPortRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigUdpPortRangeMax.setStatus(_A)
class _QamConfigOutputProgNoMin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QamConfigOutputProgNoMin_Type.__name__=_D
_QamConfigOutputProgNoMin_Object=MibTableColumn
qamConfigOutputProgNoMin=_QamConfigOutputProgNoMin_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,8),_QamConfigOutputProgNoMin_Type())
qamConfigOutputProgNoMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigOutputProgNoMin.setStatus(_A)
class _QamConfigOutputProgNoMax_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QamConfigOutputProgNoMax_Type.__name__=_D
_QamConfigOutputProgNoMax_Object=MibTableColumn
qamConfigOutputProgNoMax=_QamConfigOutputProgNoMax_Object((1,3,6,1,4,1,5591,1,11,5,3,1,1,3,1,9),_QamConfigOutputProgNoMax_Type())
qamConfigOutputProgNoMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qamConfigOutputProgNoMax.setStatus(_A)
_QamMIBConformance_ObjectIdentity=ObjectIdentity
qamMIBConformance=_QamMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,5,3,1,2))
if mibBuilder.loadTexts:qamMIBConformance.setStatus(_A)
_QamMIBCompliances_ObjectIdentity=ObjectIdentity
qamMIBCompliances=_QamMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,5,3,1,2,1))
if mibBuilder.loadTexts:qamMIBCompliances.setStatus(_A)
_QamMIBGroups_ObjectIdentity=ObjectIdentity
qamMIBGroups=_QamMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,5,3,1,2,2))
if mibBuilder.loadTexts:qamMIBGroups.setStatus(_A)
qamMpegDocsisCommonGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,5,3,1,2,2,1))
qamMpegDocsisCommonGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:qamMpegDocsisCommonGroup.setStatus(_A)
qamChannelGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,5,3,1,2,2,2))
qamChannelGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qamChannelGroup.setStatus(_A)
qamConfigGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,5,3,1,2,2,3))
qamConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:qamConfigGroup.setStatus(_A)
qamSupport=ModuleCompliance((1,3,6,1,4,1,5591,1,11,5,3,1,2,1,1))
qamSupport.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:qamSupport.setStatus(_A)
docsisSupport=ModuleCompliance((1,3,6,1,4,1,5591,1,11,5,3,1,2,1,2))
docsisSupport.setObjects((_B,_e))
if mibBuilder.loadTexts:docsisSupport.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heDigitalQamMIB':heDigitalQamMIB,'qamMIBObjects':qamMIBObjects,'qamChannelTable':qamChannelTable,'qamChannelEntry':qamChannelEntry,_M:qamChannelFrequency,_N:qamChannelModulationFormat,_O:qamChannelInterleaverLevel,_P:qamChannelInterleaverMode,_Q:qamChannelPower,_R:qamChannelSquelch,_S:qamChannelContWaveMode,_T:qamChannelAnnexMode,'qamChannelCommonTable':qamChannelCommonTable,'qamChannelCommonEntry':qamChannelCommonEntry,_K:qamChannelCommonOutputBw,_L:qamChannelCommonUtilization,'qamConfigTable':qamConfigTable,'qamConfigEntry':qamConfigEntry,_J:qamConfigIndex,_U:qamConfigQamChannelIdMin,_V:qamConfigQamChannelIdMax,_W:qamConfigIPAddrType,_X:qamConfigIPAddr,_Y:qamConfigUdpPortRangeMin,_Z:qamConfigUdpPortRangeMax,_a:qamConfigOutputProgNoMin,_b:qamConfigOutputProgNoMax,'qamMIBConformance':qamMIBConformance,'qamMIBCompliances':qamMIBCompliances,'qamSupport':qamSupport,'docsisSupport':docsisSupport,'qamMIBGroups':qamMIBGroups,_e:qamMpegDocsisCommonGroup,_c:qamChannelGroup,_d:qamConfigGroup})