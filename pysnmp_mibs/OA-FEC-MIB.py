_h='oaFecMibMandatoryStatPrevDayGroup'
_g='oaFecMibMandatoryStatCurrentDayGroup'
_f='oaFecMibMandatoryStatIntervalGroup'
_e='oaFecMibMandatoryStatCurrentGroup'
_d='oaFecMibMandatoryConfigurationGroup'
_c='oaFecPrevDayStatValidData'
_b='oaFecPrevDayStatUncorrBlocks'
_a='oaFecPrevDayStatCorrectedBits'
_Z='oaFecDayStatUncorrectedBlocks'
_Y='oaFecDayStatCorrectedBits'
_X='oaFecStatIntervalValidData'
_W='oaFecStatIntervalUncorrectedBlocks'
_V='oaFecStatIntervalCorrectedBits'
_U='oaFecStatisticsUncorrectedBlocks'
_T='oaFecStatisticsCorrectedBits'
_S='oaFecConfigurationMode'
_R='oaFecConfigurationSupportedPorts'
_Q='oaFecMibFecSlotsNumber'
_P='oaFecMibSupport'
_O='oaFecPrevDayStatPortIndex'
_N='oaFecPrevDayStatSlotIndex'
_M='oaFecDayStatPortIndex'
_L='oaFecDayStatSlotIndex'
_K='oaFecStatIntervalNumber'
_J='oaFecStatIntervalPortNumber'
_I='oaFecStatIntervalSlotNumber'
_H='oaFecStatisticsPortIndex'
_G='oaFecStatisticsSlotIndex'
_F='oaFecConfigurationSlotIndex'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='OA-FEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oaFecMib=ModuleIdentity((1,3,6,1,4,1,6926,1,19))
if mibBuilder.loadTexts:oaFecMib.setRevisions(('2007-11-25 00:00',))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaFecMibGen_ObjectIdentity=ObjectIdentity
oaFecMibGen=_OaFecMibGen_ObjectIdentity((1,3,6,1,4,1,6926,1,19,1))
class _OaFecMibSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaFecMibSupport_Type.__name__=_C
_OaFecMibSupport_Object=MibScalar
oaFecMibSupport=_OaFecMibSupport_Object((1,3,6,1,4,1,6926,1,19,1,1),_OaFecMibSupport_Type())
oaFecMibSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecMibSupport.setStatus(_A)
class _OaFecMibFecSlotsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecMibFecSlotsNumber_Type.__name__=_C
_OaFecMibFecSlotsNumber_Object=MibScalar
oaFecMibFecSlotsNumber=_OaFecMibFecSlotsNumber_Object((1,3,6,1,4,1,6926,1,19,1,2),_OaFecMibFecSlotsNumber_Type())
oaFecMibFecSlotsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecMibFecSlotsNumber.setStatus(_A)
_OaFecMibParams_ObjectIdentity=ObjectIdentity
oaFecMibParams=_OaFecMibParams_ObjectIdentity((1,3,6,1,4,1,6926,1,19,2))
_OaFecConfigurationTable_Object=MibTable
oaFecConfigurationTable=_OaFecConfigurationTable_Object((1,3,6,1,4,1,6926,1,19,2,1))
if mibBuilder.loadTexts:oaFecConfigurationTable.setStatus(_A)
_OaFecConfigurationEntry_Object=MibTableRow
oaFecConfigurationEntry=_OaFecConfigurationEntry_Object((1,3,6,1,4,1,6926,1,19,2,1,1))
oaFecConfigurationEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:oaFecConfigurationEntry.setStatus(_A)
class _OaFecConfigurationSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecConfigurationSlotIndex_Type.__name__=_C
_OaFecConfigurationSlotIndex_Object=MibTableColumn
oaFecConfigurationSlotIndex=_OaFecConfigurationSlotIndex_Object((1,3,6,1,4,1,6926,1,19,2,1,1,1),_OaFecConfigurationSlotIndex_Type())
oaFecConfigurationSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecConfigurationSlotIndex.setStatus(_A)
class _OaFecConfigurationSupportedPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecConfigurationSupportedPorts_Type.__name__=_C
_OaFecConfigurationSupportedPorts_Object=MibTableColumn
oaFecConfigurationSupportedPorts=_OaFecConfigurationSupportedPorts_Object((1,3,6,1,4,1,6926,1,19,2,1,1,2),_OaFecConfigurationSupportedPorts_Type())
oaFecConfigurationSupportedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecConfigurationSupportedPorts.setStatus(_A)
class _OaFecConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oaFecModeOther',1),('oaFecModeG709',2),('oaFecModeEfec',3)))
_OaFecConfigurationMode_Type.__name__=_C
_OaFecConfigurationMode_Object=MibTableColumn
oaFecConfigurationMode=_OaFecConfigurationMode_Object((1,3,6,1,4,1,6926,1,19,2,1,1,3),_OaFecConfigurationMode_Type())
oaFecConfigurationMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:oaFecConfigurationMode.setStatus(_A)
_OaFecStatisticsCurrentTable_Object=MibTable
oaFecStatisticsCurrentTable=_OaFecStatisticsCurrentTable_Object((1,3,6,1,4,1,6926,1,19,2,2))
if mibBuilder.loadTexts:oaFecStatisticsCurrentTable.setStatus(_A)
_OaFecStatisticsCurrentEntry_Object=MibTableRow
oaFecStatisticsCurrentEntry=_OaFecStatisticsCurrentEntry_Object((1,3,6,1,4,1,6926,1,19,2,2,1))
oaFecStatisticsCurrentEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:oaFecStatisticsCurrentEntry.setStatus(_A)
class _OaFecStatisticsSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecStatisticsSlotIndex_Type.__name__=_C
_OaFecStatisticsSlotIndex_Object=MibTableColumn
oaFecStatisticsSlotIndex=_OaFecStatisticsSlotIndex_Object((1,3,6,1,4,1,6926,1,19,2,2,1,1),_OaFecStatisticsSlotIndex_Type())
oaFecStatisticsSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecStatisticsSlotIndex.setStatus(_A)
class _OaFecStatisticsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecStatisticsPortIndex_Type.__name__=_C
_OaFecStatisticsPortIndex_Object=MibTableColumn
oaFecStatisticsPortIndex=_OaFecStatisticsPortIndex_Object((1,3,6,1,4,1,6926,1,19,2,2,1,2),_OaFecStatisticsPortIndex_Type())
oaFecStatisticsPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecStatisticsPortIndex.setStatus(_A)
_OaFecStatisticsCorrectedBits_Type=Integer32
_OaFecStatisticsCorrectedBits_Object=MibTableColumn
oaFecStatisticsCorrectedBits=_OaFecStatisticsCorrectedBits_Object((1,3,6,1,4,1,6926,1,19,2,2,1,3),_OaFecStatisticsCorrectedBits_Type())
oaFecStatisticsCorrectedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecStatisticsCorrectedBits.setStatus(_A)
_OaFecStatisticsUncorrectedBlocks_Type=Integer32
_OaFecStatisticsUncorrectedBlocks_Object=MibTableColumn
oaFecStatisticsUncorrectedBlocks=_OaFecStatisticsUncorrectedBlocks_Object((1,3,6,1,4,1,6926,1,19,2,2,1,4),_OaFecStatisticsUncorrectedBlocks_Type())
oaFecStatisticsUncorrectedBlocks.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecStatisticsUncorrectedBlocks.setStatus(_A)
_OaFecStatIntervalTable_Object=MibTable
oaFecStatIntervalTable=_OaFecStatIntervalTable_Object((1,3,6,1,4,1,6926,1,19,2,3))
if mibBuilder.loadTexts:oaFecStatIntervalTable.setStatus(_A)
_OaFecStatIntervalEntry_Object=MibTableRow
oaFecStatIntervalEntry=_OaFecStatIntervalEntry_Object((1,3,6,1,4,1,6926,1,19,2,3,1))
oaFecStatIntervalEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:oaFecStatIntervalEntry.setStatus(_A)
class _OaFecStatIntervalSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecStatIntervalSlotNumber_Type.__name__=_C
_OaFecStatIntervalSlotNumber_Object=MibTableColumn
oaFecStatIntervalSlotNumber=_OaFecStatIntervalSlotNumber_Object((1,3,6,1,4,1,6926,1,19,2,3,1,1),_OaFecStatIntervalSlotNumber_Type())
oaFecStatIntervalSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecStatIntervalSlotNumber.setStatus(_A)
class _OaFecStatIntervalPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecStatIntervalPortNumber_Type.__name__=_C
_OaFecStatIntervalPortNumber_Object=MibTableColumn
oaFecStatIntervalPortNumber=_OaFecStatIntervalPortNumber_Object((1,3,6,1,4,1,6926,1,19,2,3,1,2),_OaFecStatIntervalPortNumber_Type())
oaFecStatIntervalPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecStatIntervalPortNumber.setStatus(_A)
class _OaFecStatIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_OaFecStatIntervalNumber_Type.__name__=_C
_OaFecStatIntervalNumber_Object=MibTableColumn
oaFecStatIntervalNumber=_OaFecStatIntervalNumber_Object((1,3,6,1,4,1,6926,1,19,2,3,1,3),_OaFecStatIntervalNumber_Type())
oaFecStatIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecStatIntervalNumber.setStatus(_A)
_OaFecStatIntervalCorrectedBits_Type=Integer32
_OaFecStatIntervalCorrectedBits_Object=MibTableColumn
oaFecStatIntervalCorrectedBits=_OaFecStatIntervalCorrectedBits_Object((1,3,6,1,4,1,6926,1,19,2,3,1,4),_OaFecStatIntervalCorrectedBits_Type())
oaFecStatIntervalCorrectedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecStatIntervalCorrectedBits.setStatus(_A)
_OaFecStatIntervalUncorrectedBlocks_Type=Integer32
_OaFecStatIntervalUncorrectedBlocks_Object=MibTableColumn
oaFecStatIntervalUncorrectedBlocks=_OaFecStatIntervalUncorrectedBlocks_Object((1,3,6,1,4,1,6926,1,19,2,3,1,5),_OaFecStatIntervalUncorrectedBlocks_Type())
oaFecStatIntervalUncorrectedBlocks.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecStatIntervalUncorrectedBlocks.setStatus(_A)
_OaFecStatIntervalValidData_Type=TruthValue
_OaFecStatIntervalValidData_Object=MibTableColumn
oaFecStatIntervalValidData=_OaFecStatIntervalValidData_Object((1,3,6,1,4,1,6926,1,19,2,3,1,6),_OaFecStatIntervalValidData_Type())
oaFecStatIntervalValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecStatIntervalValidData.setStatus(_A)
_OaFecStatCurrentDayTable_Object=MibTable
oaFecStatCurrentDayTable=_OaFecStatCurrentDayTable_Object((1,3,6,1,4,1,6926,1,19,2,4))
if mibBuilder.loadTexts:oaFecStatCurrentDayTable.setStatus(_A)
_OaFecStatCurrentDayEntry_Object=MibTableRow
oaFecStatCurrentDayEntry=_OaFecStatCurrentDayEntry_Object((1,3,6,1,4,1,6926,1,19,2,4,1))
oaFecStatCurrentDayEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:oaFecStatCurrentDayEntry.setStatus(_A)
class _OaFecDayStatSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecDayStatSlotIndex_Type.__name__=_C
_OaFecDayStatSlotIndex_Object=MibTableColumn
oaFecDayStatSlotIndex=_OaFecDayStatSlotIndex_Object((1,3,6,1,4,1,6926,1,19,2,4,1,1),_OaFecDayStatSlotIndex_Type())
oaFecDayStatSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecDayStatSlotIndex.setStatus(_A)
class _OaFecDayStatPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecDayStatPortIndex_Type.__name__=_C
_OaFecDayStatPortIndex_Object=MibTableColumn
oaFecDayStatPortIndex=_OaFecDayStatPortIndex_Object((1,3,6,1,4,1,6926,1,19,2,4,1,2),_OaFecDayStatPortIndex_Type())
oaFecDayStatPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecDayStatPortIndex.setStatus(_A)
_OaFecDayStatCorrectedBits_Type=Integer32
_OaFecDayStatCorrectedBits_Object=MibTableColumn
oaFecDayStatCorrectedBits=_OaFecDayStatCorrectedBits_Object((1,3,6,1,4,1,6926,1,19,2,4,1,3),_OaFecDayStatCorrectedBits_Type())
oaFecDayStatCorrectedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecDayStatCorrectedBits.setStatus(_A)
_OaFecDayStatUncorrectedBlocks_Type=Integer32
_OaFecDayStatUncorrectedBlocks_Object=MibTableColumn
oaFecDayStatUncorrectedBlocks=_OaFecDayStatUncorrectedBlocks_Object((1,3,6,1,4,1,6926,1,19,2,4,1,4),_OaFecDayStatUncorrectedBlocks_Type())
oaFecDayStatUncorrectedBlocks.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecDayStatUncorrectedBlocks.setStatus(_A)
_OaFecStatPrevDayTable_Object=MibTable
oaFecStatPrevDayTable=_OaFecStatPrevDayTable_Object((1,3,6,1,4,1,6926,1,19,2,5))
if mibBuilder.loadTexts:oaFecStatPrevDayTable.setStatus(_A)
_OaFecStatPrevDayEntry_Object=MibTableRow
oaFecStatPrevDayEntry=_OaFecStatPrevDayEntry_Object((1,3,6,1,4,1,6926,1,19,2,5,1))
oaFecStatPrevDayEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:oaFecStatPrevDayEntry.setStatus(_A)
class _OaFecPrevDayStatSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecPrevDayStatSlotIndex_Type.__name__=_C
_OaFecPrevDayStatSlotIndex_Object=MibTableColumn
oaFecPrevDayStatSlotIndex=_OaFecPrevDayStatSlotIndex_Object((1,3,6,1,4,1,6926,1,19,2,5,1,1),_OaFecPrevDayStatSlotIndex_Type())
oaFecPrevDayStatSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecPrevDayStatSlotIndex.setStatus(_A)
class _OaFecPrevDayStatPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaFecPrevDayStatPortIndex_Type.__name__=_C
_OaFecPrevDayStatPortIndex_Object=MibTableColumn
oaFecPrevDayStatPortIndex=_OaFecPrevDayStatPortIndex_Object((1,3,6,1,4,1,6926,1,19,2,5,1,2),_OaFecPrevDayStatPortIndex_Type())
oaFecPrevDayStatPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:oaFecPrevDayStatPortIndex.setStatus(_A)
_OaFecPrevDayStatCorrectedBits_Type=Integer32
_OaFecPrevDayStatCorrectedBits_Object=MibTableColumn
oaFecPrevDayStatCorrectedBits=_OaFecPrevDayStatCorrectedBits_Object((1,3,6,1,4,1,6926,1,19,2,5,1,3),_OaFecPrevDayStatCorrectedBits_Type())
oaFecPrevDayStatCorrectedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecPrevDayStatCorrectedBits.setStatus(_A)
_OaFecPrevDayStatUncorrBlocks_Type=Integer32
_OaFecPrevDayStatUncorrBlocks_Object=MibTableColumn
oaFecPrevDayStatUncorrBlocks=_OaFecPrevDayStatUncorrBlocks_Object((1,3,6,1,4,1,6926,1,19,2,5,1,4),_OaFecPrevDayStatUncorrBlocks_Type())
oaFecPrevDayStatUncorrBlocks.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecPrevDayStatUncorrBlocks.setStatus(_A)
_OaFecPrevDayStatValidData_Type=TruthValue
_OaFecPrevDayStatValidData_Object=MibTableColumn
oaFecPrevDayStatValidData=_OaFecPrevDayStatValidData_Object((1,3,6,1,4,1,6926,1,19,2,5,1,5),_OaFecPrevDayStatValidData_Type())
oaFecPrevDayStatValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:oaFecPrevDayStatValidData.setStatus(_A)
_OaFecMibConformance_ObjectIdentity=ObjectIdentity
oaFecMibConformance=_OaFecMibConformance_ObjectIdentity((1,3,6,1,4,1,6926,1,19,101))
_OaFecMibMIBCompliances_ObjectIdentity=ObjectIdentity
oaFecMibMIBCompliances=_OaFecMibMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,1,19,101,1))
_OaFecMibMIBGroups_ObjectIdentity=ObjectIdentity
oaFecMibMIBGroups=_OaFecMibMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,1,19,101,2))
oaFecMibMandatoryConfigurationGroup=ObjectGroup((1,3,6,1,4,1,6926,1,19,101,2,1))
oaFecMibMandatoryConfigurationGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:oaFecMibMandatoryConfigurationGroup.setStatus(_A)
oaFecMibMandatoryStatCurrentGroup=ObjectGroup((1,3,6,1,4,1,6926,1,19,101,2,2))
oaFecMibMandatoryStatCurrentGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:oaFecMibMandatoryStatCurrentGroup.setStatus(_A)
oaFecMibMandatoryStatIntervalGroup=ObjectGroup((1,3,6,1,4,1,6926,1,19,101,2,3))
oaFecMibMandatoryStatIntervalGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:oaFecMibMandatoryStatIntervalGroup.setStatus(_A)
oaFecMibMandatoryStatCurrentDayGroup=ObjectGroup((1,3,6,1,4,1,6926,1,19,101,2,4))
oaFecMibMandatoryStatCurrentDayGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:oaFecMibMandatoryStatCurrentDayGroup.setStatus(_A)
oaFecMibMandatoryStatPrevDayGroup=ObjectGroup((1,3,6,1,4,1,6926,1,19,101,2,5))
oaFecMibMandatoryStatPrevDayGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:oaFecMibMandatoryStatPrevDayGroup.setStatus(_A)
oaFecMibMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,1,19,101,1,1))
oaFecMibMIBCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:oaFecMibMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oaccess':oaccess,'oaManagement':oaManagement,'oaFecMib':oaFecMib,'oaFecMibGen':oaFecMibGen,_P:oaFecMibSupport,_Q:oaFecMibFecSlotsNumber,'oaFecMibParams':oaFecMibParams,'oaFecConfigurationTable':oaFecConfigurationTable,'oaFecConfigurationEntry':oaFecConfigurationEntry,_F:oaFecConfigurationSlotIndex,_R:oaFecConfigurationSupportedPorts,_S:oaFecConfigurationMode,'oaFecStatisticsCurrentTable':oaFecStatisticsCurrentTable,'oaFecStatisticsCurrentEntry':oaFecStatisticsCurrentEntry,_G:oaFecStatisticsSlotIndex,_H:oaFecStatisticsPortIndex,_T:oaFecStatisticsCorrectedBits,_U:oaFecStatisticsUncorrectedBlocks,'oaFecStatIntervalTable':oaFecStatIntervalTable,'oaFecStatIntervalEntry':oaFecStatIntervalEntry,_I:oaFecStatIntervalSlotNumber,_J:oaFecStatIntervalPortNumber,_K:oaFecStatIntervalNumber,_V:oaFecStatIntervalCorrectedBits,_W:oaFecStatIntervalUncorrectedBlocks,_X:oaFecStatIntervalValidData,'oaFecStatCurrentDayTable':oaFecStatCurrentDayTable,'oaFecStatCurrentDayEntry':oaFecStatCurrentDayEntry,_L:oaFecDayStatSlotIndex,_M:oaFecDayStatPortIndex,_Y:oaFecDayStatCorrectedBits,_Z:oaFecDayStatUncorrectedBlocks,'oaFecStatPrevDayTable':oaFecStatPrevDayTable,'oaFecStatPrevDayEntry':oaFecStatPrevDayEntry,_N:oaFecPrevDayStatSlotIndex,_O:oaFecPrevDayStatPortIndex,_a:oaFecPrevDayStatCorrectedBits,_b:oaFecPrevDayStatUncorrBlocks,_c:oaFecPrevDayStatValidData,'oaFecMibConformance':oaFecMibConformance,'oaFecMibMIBCompliances':oaFecMibMIBCompliances,'oaFecMibMIBCompliance':oaFecMibMIBCompliance,'oaFecMibMIBGroups':oaFecMibMIBGroups,_d:oaFecMibMandatoryConfigurationGroup,_e:oaFecMibMandatoryStatCurrentGroup,_f:oaFecMibMandatoryStatIntervalGroup,_g:oaFecMibMandatoryStatCurrentDayGroup,_h:oaFecMibMandatoryStatPrevDayGroup})