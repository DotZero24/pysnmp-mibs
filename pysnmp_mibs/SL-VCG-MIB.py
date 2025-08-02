_N='vcgStackLcasStatusOper'
_M='vcgLinkDayNumber'
_L='vcgLinkDayIndex'
_K='vcgLinkIntervalNumber'
_J='vcgLinkIntervalIndex'
_I='vcgLinkCurrentIndex'
_H='vcgLinkConfigIndex'
_G='vcgStackStsIndex'
_F='vcgStackLinkIndex'
_E='Integer32'
_D='SL-VCG-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
vcgMIB=ModuleIdentity((1,3,6,1,4,1,4515,1,1,10))
class VcgLinkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('framed',1),('transparent',2),('pos',3)))
_VcgMIBObjects_ObjectIdentity=ObjectIdentity
vcgMIBObjects=_VcgMIBObjects_ObjectIdentity((1,3,6,1,4,1,4515,1,1,10,1))
_VcgConfig_ObjectIdentity=ObjectIdentity
vcgConfig=_VcgConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,10,1,1))
_VcgStackStatusTable_Object=MibTable
vcgStackStatusTable=_VcgStackStatusTable_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1))
if mibBuilder.loadTexts:vcgStackStatusTable.setStatus(_A)
_VcgStackStatusEntry_Object=MibTableRow
vcgStackStatusEntry=_VcgStackStatusEntry_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1))
vcgStackStatusEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:vcgStackStatusEntry.setStatus(_A)
_VcgStackLinkIndex_Type=InterfaceIndex
_VcgStackLinkIndex_Object=MibTableColumn
vcgStackLinkIndex=_VcgStackLinkIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,1),_VcgStackLinkIndex_Type())
vcgStackLinkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgStackLinkIndex.setStatus(_A)
_VcgStackStsIndex_Type=InterfaceIndex
_VcgStackStsIndex_Object=MibTableColumn
vcgStackStsIndex=_VcgStackStsIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,2),_VcgStackStsIndex_Type())
vcgStackStsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgStackStsIndex.setStatus(_A)
class _VcgStackPathWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,11,12)));namedValues=NamedValues(*(('vtWidth45STS1',1),('vtWidth155STS3',3),('vtWidth15VC11',11),('vtWidth2VC12',12)))
_VcgStackPathWidth_Type.__name__=_E
_VcgStackPathWidth_Object=MibTableColumn
vcgStackPathWidth=_VcgStackPathWidth_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,3),_VcgStackPathWidth_Type())
vcgStackPathWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackPathWidth.setStatus(_A)
class _VcgStackSts1Mapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tu3',1),('au3',2),('na',3)))
_VcgStackSts1Mapping_Type.__name__=_E
_VcgStackSts1Mapping_Object=MibTableColumn
vcgStackSts1Mapping=_VcgStackSts1Mapping_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,4),_VcgStackSts1Mapping_Type())
vcgStackSts1Mapping.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackSts1Mapping.setStatus(_A)
_VcgStackTxSequenceNumber_Type=Integer32
_VcgStackTxSequenceNumber_Object=MibTableColumn
vcgStackTxSequenceNumber=_VcgStackTxSequenceNumber_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,5),_VcgStackTxSequenceNumber_Type())
vcgStackTxSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackTxSequenceNumber.setStatus(_A)
class _VcgStackLcasStatusOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VcgStackLcasStatusOper_Type.__name__=_E
_VcgStackLcasStatusOper_Object=MibTableColumn
vcgStackLcasStatusOper=_VcgStackLcasStatusOper_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,6),_VcgStackLcasStatusOper_Type())
vcgStackLcasStatusOper.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackLcasStatusOper.setStatus(_A)
class _VcgStackLcasStatusAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('nonActive',2)))
_VcgStackLcasStatusAdmin_Type.__name__=_E
_VcgStackLcasStatusAdmin_Object=MibTableColumn
vcgStackLcasStatusAdmin=_VcgStackLcasStatusAdmin_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,7),_VcgStackLcasStatusAdmin_Type())
vcgStackLcasStatusAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackLcasStatusAdmin.setStatus(_A)
class _VcgStackLcasSourceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('norm',1),('dnu',2),('add',3),('idle',4)))
_VcgStackLcasSourceState_Type.__name__=_E
_VcgStackLcasSourceState_Object=MibTableColumn
vcgStackLcasSourceState=_VcgStackLcasSourceState_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,8),_VcgStackLcasSourceState_Type())
vcgStackLcasSourceState.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackLcasSourceState.setStatus(_A)
class _VcgStackLcasSinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('fail',2),('idle',3)))
_VcgStackLcasSinkState_Type.__name__=_E
_VcgStackLcasSinkState_Object=MibTableColumn
vcgStackLcasSinkState=_VcgStackLcasSinkState_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,9),_VcgStackLcasSinkState_Type())
vcgStackLcasSinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackLcasSinkState.setStatus(_A)
_VcgStackStatusRow_Type=RowStatus
_VcgStackStatusRow_Object=MibTableColumn
vcgStackStatusRow=_VcgStackStatusRow_Object((1,3,6,1,4,1,4515,1,1,10,1,1,1,1,10),_VcgStackStatusRow_Type())
vcgStackStatusRow.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgStackStatusRow.setStatus(_A)
_VcgLinkConfigTable_Object=MibTable
vcgLinkConfigTable=_VcgLinkConfigTable_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2))
if mibBuilder.loadTexts:vcgLinkConfigTable.setStatus(_A)
_VcgLinkConfigEntry_Object=MibTableRow
vcgLinkConfigEntry=_VcgLinkConfigEntry_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1))
vcgLinkConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:vcgLinkConfigEntry.setStatus(_A)
_VcgLinkConfigIndex_Type=InterfaceIndex
_VcgLinkConfigIndex_Object=MibTableColumn
vcgLinkConfigIndex=_VcgLinkConfigIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,1),_VcgLinkConfigIndex_Type())
vcgLinkConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkConfigIndex.setStatus(_A)
_VcgLinkConfigType_Type=VcgLinkType
_VcgLinkConfigType_Object=MibTableColumn
vcgLinkConfigType=_VcgLinkConfigType_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,2),_VcgLinkConfigType_Type())
vcgLinkConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigType.setStatus(_A)
_VcgLinkConfigLcasSupport_Type=TruthValue
_VcgLinkConfigLcasSupport_Object=MibTableColumn
vcgLinkConfigLcasSupport=_VcgLinkConfigLcasSupport_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,3),_VcgLinkConfigLcasSupport_Type())
vcgLinkConfigLcasSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigLcasSupport.setStatus(_A)
_VcgLinkConfigExtensionSupport_Type=TruthValue
_VcgLinkConfigExtensionSupport_Object=MibTableColumn
vcgLinkConfigExtensionSupport=_VcgLinkConfigExtensionSupport_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,4),_VcgLinkConfigExtensionSupport_Type())
vcgLinkConfigExtensionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigExtensionSupport.setStatus(_A)
_VcgLinkConfigResetPmCounters_Type=Integer32
_VcgLinkConfigResetPmCounters_Object=MibTableColumn
vcgLinkConfigResetPmCounters=_VcgLinkConfigResetPmCounters_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,5),_VcgLinkConfigResetPmCounters_Type())
vcgLinkConfigResetPmCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigResetPmCounters.setStatus(_A)
class _VcgLinkConfigValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_VcgLinkConfigValidIntervals_Type.__name__=_E
_VcgLinkConfigValidIntervals_Object=MibTableColumn
vcgLinkConfigValidIntervals=_VcgLinkConfigValidIntervals_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,6),_VcgLinkConfigValidIntervals_Type())
vcgLinkConfigValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkConfigValidIntervals.setStatus(_A)
_VcgLinkConfigLcasHoldOfTime_Type=Integer32
_VcgLinkConfigLcasHoldOfTime_Object=MibTableColumn
vcgLinkConfigLcasHoldOfTime=_VcgLinkConfigLcasHoldOfTime_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,7),_VcgLinkConfigLcasHoldOfTime_Type())
vcgLinkConfigLcasHoldOfTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigLcasHoldOfTime.setStatus(_A)
_VcgLinkConfigLcasWaitToRestoreTime_Type=Integer32
_VcgLinkConfigLcasWaitToRestoreTime_Object=MibTableColumn
vcgLinkConfigLcasWaitToRestoreTime=_VcgLinkConfigLcasWaitToRestoreTime_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,8),_VcgLinkConfigLcasWaitToRestoreTime_Type())
vcgLinkConfigLcasWaitToRestoreTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigLcasWaitToRestoreTime.setStatus(_A)
_VcgLinkConfigStackApplyChanges_Type=Integer32
_VcgLinkConfigStackApplyChanges_Object=MibTableColumn
vcgLinkConfigStackApplyChanges=_VcgLinkConfigStackApplyChanges_Object((1,3,6,1,4,1,4515,1,1,10,1,1,2,1,9),_VcgLinkConfigStackApplyChanges_Type())
vcgLinkConfigStackApplyChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLinkConfigStackApplyChanges.setStatus(_A)
_VcgPm_ObjectIdentity=ObjectIdentity
vcgPm=_VcgPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,10,1,2))
_VcgLinkCurrentTable_Object=MibTable
vcgLinkCurrentTable=_VcgLinkCurrentTable_Object((1,3,6,1,4,1,4515,1,1,10,1,2,1))
if mibBuilder.loadTexts:vcgLinkCurrentTable.setStatus(_A)
_VcgLinkCurrentEntry_Object=MibTableRow
vcgLinkCurrentEntry=_VcgLinkCurrentEntry_Object((1,3,6,1,4,1,4515,1,1,10,1,2,1,1))
vcgLinkCurrentEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:vcgLinkCurrentEntry.setStatus(_A)
_VcgLinkCurrentIndex_Type=InterfaceIndex
_VcgLinkCurrentIndex_Object=MibTableColumn
vcgLinkCurrentIndex=_VcgLinkCurrentIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,2,1,1,1),_VcgLinkCurrentIndex_Type())
vcgLinkCurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkCurrentIndex.setStatus(_A)
_VcgLinkCurrentRxVcatSyncLossSeconds_Type=Counter64
_VcgLinkCurrentRxVcatSyncLossSeconds_Object=MibTableColumn
vcgLinkCurrentRxVcatSyncLossSeconds=_VcgLinkCurrentRxVcatSyncLossSeconds_Object((1,3,6,1,4,1,4515,1,1,10,1,2,1,1,2),_VcgLinkCurrentRxVcatSyncLossSeconds_Type())
vcgLinkCurrentRxVcatSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkCurrentRxVcatSyncLossSeconds.setStatus(_A)
_VcgLinkCurrentRxLcasCrcErrors_Type=Counter64
_VcgLinkCurrentRxLcasCrcErrors_Object=MibTableColumn
vcgLinkCurrentRxLcasCrcErrors=_VcgLinkCurrentRxLcasCrcErrors_Object((1,3,6,1,4,1,4515,1,1,10,1,2,1,1,3),_VcgLinkCurrentRxLcasCrcErrors_Type())
vcgLinkCurrentRxLcasCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkCurrentRxLcasCrcErrors.setStatus(_A)
_VcgLinkIntervalTable_Object=MibTable
vcgLinkIntervalTable=_VcgLinkIntervalTable_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2))
if mibBuilder.loadTexts:vcgLinkIntervalTable.setStatus(_A)
_VcgLinkIntervalEntry_Object=MibTableRow
vcgLinkIntervalEntry=_VcgLinkIntervalEntry_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2,1))
vcgLinkIntervalEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:vcgLinkIntervalEntry.setStatus(_A)
_VcgLinkIntervalIndex_Type=InterfaceIndex
_VcgLinkIntervalIndex_Object=MibTableColumn
vcgLinkIntervalIndex=_VcgLinkIntervalIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2,1,1),_VcgLinkIntervalIndex_Type())
vcgLinkIntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkIntervalIndex.setStatus(_A)
class _VcgLinkIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_VcgLinkIntervalNumber_Type.__name__=_E
_VcgLinkIntervalNumber_Object=MibTableColumn
vcgLinkIntervalNumber=_VcgLinkIntervalNumber_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2,1,2),_VcgLinkIntervalNumber_Type())
vcgLinkIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkIntervalNumber.setStatus(_A)
_VcgLinkIntervalRxVcatSyncLossSeconds_Type=Counter64
_VcgLinkIntervalRxVcatSyncLossSeconds_Object=MibTableColumn
vcgLinkIntervalRxVcatSyncLossSeconds=_VcgLinkIntervalRxVcatSyncLossSeconds_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2,1,3),_VcgLinkIntervalRxVcatSyncLossSeconds_Type())
vcgLinkIntervalRxVcatSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkIntervalRxVcatSyncLossSeconds.setStatus(_A)
_VcgLinkIntervalRxLcasCrcErrors_Type=Counter64
_VcgLinkIntervalRxLcasCrcErrors_Object=MibTableColumn
vcgLinkIntervalRxLcasCrcErrors=_VcgLinkIntervalRxLcasCrcErrors_Object((1,3,6,1,4,1,4515,1,1,10,1,2,2,1,4),_VcgLinkIntervalRxLcasCrcErrors_Type())
vcgLinkIntervalRxLcasCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkIntervalRxLcasCrcErrors.setStatus(_A)
_VcgLinkDayTable_Object=MibTable
vcgLinkDayTable=_VcgLinkDayTable_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3))
if mibBuilder.loadTexts:vcgLinkDayTable.setStatus(_A)
_VcgLinkDayEntry_Object=MibTableRow
vcgLinkDayEntry=_VcgLinkDayEntry_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3,1))
vcgLinkDayEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:vcgLinkDayEntry.setStatus(_A)
_VcgLinkDayIndex_Type=InterfaceIndex
_VcgLinkDayIndex_Object=MibTableColumn
vcgLinkDayIndex=_VcgLinkDayIndex_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3,1,1),_VcgLinkDayIndex_Type())
vcgLinkDayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkDayIndex.setStatus(_A)
class _VcgLinkDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_VcgLinkDayNumber_Type.__name__=_E
_VcgLinkDayNumber_Object=MibTableColumn
vcgLinkDayNumber=_VcgLinkDayNumber_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3,1,2),_VcgLinkDayNumber_Type())
vcgLinkDayNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vcgLinkDayNumber.setStatus(_A)
_VcgLinkDayRxVcatSyncLossSeconds_Type=Counter64
_VcgLinkDayRxVcatSyncLossSeconds_Object=MibTableColumn
vcgLinkDayRxVcatSyncLossSeconds=_VcgLinkDayRxVcatSyncLossSeconds_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3,1,3),_VcgLinkDayRxVcatSyncLossSeconds_Type())
vcgLinkDayRxVcatSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkDayRxVcatSyncLossSeconds.setStatus(_A)
_VcgLinkDayRxLcasCrcErrors_Type=Counter64
_VcgLinkDayRxLcasCrcErrors_Object=MibTableColumn
vcgLinkDayRxLcasCrcErrors=_VcgLinkDayRxLcasCrcErrors_Object((1,3,6,1,4,1,4515,1,1,10,1,2,3,1,4),_VcgLinkDayRxLcasCrcErrors_Type())
vcgLinkDayRxLcasCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgLinkDayRxLcasCrcErrors.setStatus(_A)
_VcgTraps_ObjectIdentity=ObjectIdentity
vcgTraps=_VcgTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,10,1,3))
vcgStackValueChange=NotificationType((1,3,6,1,4,1,4515,1,1,10,1,3,1))
vcgStackValueChange.setObjects(*((_D,_F),(_D,_G),(_D,_N)))
if mibBuilder.loadTexts:vcgStackValueChange.setStatus(_A)
vcgStackConfigurationChange=NotificationType((1,3,6,1,4,1,4515,1,1,10,1,3,2))
if mibBuilder.loadTexts:vcgStackConfigurationChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VcgLinkType':VcgLinkType,'vcgMIB':vcgMIB,'vcgMIBObjects':vcgMIBObjects,'vcgConfig':vcgConfig,'vcgStackStatusTable':vcgStackStatusTable,'vcgStackStatusEntry':vcgStackStatusEntry,_F:vcgStackLinkIndex,_G:vcgStackStsIndex,'vcgStackPathWidth':vcgStackPathWidth,'vcgStackSts1Mapping':vcgStackSts1Mapping,'vcgStackTxSequenceNumber':vcgStackTxSequenceNumber,_N:vcgStackLcasStatusOper,'vcgStackLcasStatusAdmin':vcgStackLcasStatusAdmin,'vcgStackLcasSourceState':vcgStackLcasSourceState,'vcgStackLcasSinkState':vcgStackLcasSinkState,'vcgStackStatusRow':vcgStackStatusRow,'vcgLinkConfigTable':vcgLinkConfigTable,'vcgLinkConfigEntry':vcgLinkConfigEntry,_H:vcgLinkConfigIndex,'vcgLinkConfigType':vcgLinkConfigType,'vcgLinkConfigLcasSupport':vcgLinkConfigLcasSupport,'vcgLinkConfigExtensionSupport':vcgLinkConfigExtensionSupport,'vcgLinkConfigResetPmCounters':vcgLinkConfigResetPmCounters,'vcgLinkConfigValidIntervals':vcgLinkConfigValidIntervals,'vcgLinkConfigLcasHoldOfTime':vcgLinkConfigLcasHoldOfTime,'vcgLinkConfigLcasWaitToRestoreTime':vcgLinkConfigLcasWaitToRestoreTime,'vcgLinkConfigStackApplyChanges':vcgLinkConfigStackApplyChanges,'vcgPm':vcgPm,'vcgLinkCurrentTable':vcgLinkCurrentTable,'vcgLinkCurrentEntry':vcgLinkCurrentEntry,_I:vcgLinkCurrentIndex,'vcgLinkCurrentRxVcatSyncLossSeconds':vcgLinkCurrentRxVcatSyncLossSeconds,'vcgLinkCurrentRxLcasCrcErrors':vcgLinkCurrentRxLcasCrcErrors,'vcgLinkIntervalTable':vcgLinkIntervalTable,'vcgLinkIntervalEntry':vcgLinkIntervalEntry,_J:vcgLinkIntervalIndex,_K:vcgLinkIntervalNumber,'vcgLinkIntervalRxVcatSyncLossSeconds':vcgLinkIntervalRxVcatSyncLossSeconds,'vcgLinkIntervalRxLcasCrcErrors':vcgLinkIntervalRxLcasCrcErrors,'vcgLinkDayTable':vcgLinkDayTable,'vcgLinkDayEntry':vcgLinkDayEntry,_L:vcgLinkDayIndex,_M:vcgLinkDayNumber,'vcgLinkDayRxVcatSyncLossSeconds':vcgLinkDayRxVcatSyncLossSeconds,'vcgLinkDayRxLcasCrcErrors':vcgLinkDayRxLcasCrcErrors,'vcgTraps':vcgTraps,'vcgStackValueChange':vcgStackValueChange,'vcgStackConfigurationChange':vcgStackConfigurationChange})