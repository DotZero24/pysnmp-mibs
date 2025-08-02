_q='ciscoWanNcdpAtmGroup'
_p='ciscoWanNcdpManualGroup'
_o='ciscoWanNcdpClockSourceGroup'
_n='ciscoWanNcdpGlobalGroup'
_m='cwnAtmInterfaceVci'
_l='cwnAtmInterfaceVpi'
_k='cwnAtmInterfaceAdminWeight'
_j='cwnAtmInterfaceEnable'
_i='cwnAtmSourceRowStatus'
_h='cwnAtmSourceClockHealth'
_g='cwnAtmSourcePRSReference'
_f='cwnAtmSourceStratum'
_e='cwnAtmSourcePriority'
_d='cwnAtmSourceBestClockSource'
_c='cwnManualRowStatus'
_b='cwnManualClockHealth'
_a='cwnManualSourceIndex'
_Z='cwnOtherClockSource'
_Y='cwnInterfaceIndex'
_X='cwnClockSourceDesc'
_W='cwnRootClockSource'
_V='cwnChangeTimeStamp'
_U='cwnChangeReason'
_T='cwnHoldTime'
_S='cwnMessageInterval'
_R='cwnMaxDiameter'
_Q='cwnNodeStratum'
_P='cwnDistributionMethod'
_O='cwnManualSourcePriority'
_N='not-accessible'
_M='milliseconds'
_L='TruthValue'
_K='TimeStamp'
_J='ifIndex'
_I='IF-MIB'
_H='cwnClockSourceIndex'
_G='ClockStratum'
_F='read-create'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-WAN-NCDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndexOrZero',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K,_L)
ciscoWanNcdpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,223))
if mibBuilder.loadTexts:ciscoWanNcdpMIB.setRevisions(('2001-11-07 00:00',))
class ClockStratum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('s1',2),('s2e',3),('s2',4),('s3e',5),('s3',6),('s4e',7),('s4',8)))
class ClockHealthStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('bad',2),('unknown',3)))
class ClockSourceIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwnMIBObjects_ObjectIdentity=ObjectIdentity
cwnMIBObjects=_CwnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,223,1))
_CwnGlobal_ObjectIdentity=ObjectIdentity
cwnGlobal=_CwnGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,223,1,1))
class _CwnDistributionMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ncdp',1),('manual',2)))
_CwnDistributionMethod_Type.__name__=_C
_CwnDistributionMethod_Object=MibScalar
cwnDistributionMethod=_CwnDistributionMethod_Object((1,3,6,1,4,1,9,9,223,1,1,1),_CwnDistributionMethod_Type())
cwnDistributionMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnDistributionMethod.setStatus(_A)
class _CwnNodeStratum_Type(ClockStratum):defaultValue=4
_CwnNodeStratum_Type.__name__=_G
_CwnNodeStratum_Object=MibScalar
cwnNodeStratum=_CwnNodeStratum_Object((1,3,6,1,4,1,9,9,223,1,1,2),_CwnNodeStratum_Type())
cwnNodeStratum.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnNodeStratum.setStatus(_A)
class _CwnMaxDiameter_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_CwnMaxDiameter_Type.__name__=_C
_CwnMaxDiameter_Object=MibScalar
cwnMaxDiameter=_CwnMaxDiameter_Object((1,3,6,1,4,1,9,9,223,1,1,3),_CwnMaxDiameter_Type())
cwnMaxDiameter.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnMaxDiameter.setStatus(_A)
class _CwnMessageInterval_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,60000))
_CwnMessageInterval_Type.__name__=_C
_CwnMessageInterval_Object=MibScalar
cwnMessageInterval=_CwnMessageInterval_Object((1,3,6,1,4,1,9,9,223,1,1,4),_CwnMessageInterval_Type())
cwnMessageInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnMessageInterval.setStatus(_A)
if mibBuilder.loadTexts:cwnMessageInterval.setUnits(_M)
class _CwnHoldTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,60000))
_CwnHoldTime_Type.__name__=_C
_CwnHoldTime_Object=MibScalar
cwnHoldTime=_CwnHoldTime_Object((1,3,6,1,4,1,9,9,223,1,1,5),_CwnHoldTime_Type())
cwnHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cwnHoldTime.setUnits(_M)
class _CwnChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('none',2),('lossOfLock',3),('lossOfActivity',4),('ncdpRestructure',5)))
_CwnChangeReason_Type.__name__=_C
_CwnChangeReason_Object=MibScalar
cwnChangeReason=_CwnChangeReason_Object((1,3,6,1,4,1,9,9,223,1,1,6),_CwnChangeReason_Type())
cwnChangeReason.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnChangeReason.setStatus(_A)
class _CwnChangeTimeStamp_Type(TimeStamp):defaultValue=0
_CwnChangeTimeStamp_Type.__name__=_K
_CwnChangeTimeStamp_Object=MibScalar
cwnChangeTimeStamp=_CwnChangeTimeStamp_Object((1,3,6,1,4,1,9,9,223,1,1,7),_CwnChangeTimeStamp_Type())
cwnChangeTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnChangeTimeStamp.setStatus(_A)
_CwnRootClockSource_Type=ClockSourceIndex
_CwnRootClockSource_Object=MibScalar
cwnRootClockSource=_CwnRootClockSource_Object((1,3,6,1,4,1,9,9,223,1,1,8),_CwnRootClockSource_Type())
cwnRootClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnRootClockSource.setStatus(_A)
_CwnClockSource_ObjectIdentity=ObjectIdentity
cwnClockSource=_CwnClockSource_ObjectIdentity((1,3,6,1,4,1,9,9,223,1,2))
_CwnClockSourceTable_Object=MibTable
cwnClockSourceTable=_CwnClockSourceTable_Object((1,3,6,1,4,1,9,9,223,1,2,1))
if mibBuilder.loadTexts:cwnClockSourceTable.setStatus(_A)
_CwnClockSourceEntry_Object=MibTableRow
cwnClockSourceEntry=_CwnClockSourceEntry_Object((1,3,6,1,4,1,9,9,223,1,2,1,1))
cwnClockSourceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwnClockSourceEntry.setStatus(_A)
_CwnClockSourceIndex_Type=ClockSourceIndex
_CwnClockSourceIndex_Object=MibTableColumn
cwnClockSourceIndex=_CwnClockSourceIndex_Object((1,3,6,1,4,1,9,9,223,1,2,1,1,1),_CwnClockSourceIndex_Type())
cwnClockSourceIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cwnClockSourceIndex.setStatus(_A)
_CwnClockSourceDesc_Type=DisplayString
_CwnClockSourceDesc_Object=MibTableColumn
cwnClockSourceDesc=_CwnClockSourceDesc_Object((1,3,6,1,4,1,9,9,223,1,2,1,1,2),_CwnClockSourceDesc_Type())
cwnClockSourceDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnClockSourceDesc.setStatus(_A)
_CwnInterfaceIndex_Type=InterfaceIndexOrZero
_CwnInterfaceIndex_Object=MibTableColumn
cwnInterfaceIndex=_CwnInterfaceIndex_Object((1,3,6,1,4,1,9,9,223,1,2,1,1,3),_CwnInterfaceIndex_Type())
cwnInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnInterfaceIndex.setStatus(_A)
class _CwnOtherClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('internalOscillator',2),('bitsClockE1',3),('bitsClockT1',4)))
_CwnOtherClockSource_Type.__name__=_C
_CwnOtherClockSource_Object=MibTableColumn
cwnOtherClockSource=_CwnOtherClockSource_Object((1,3,6,1,4,1,9,9,223,1,2,1,1,4),_CwnOtherClockSource_Type())
cwnOtherClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnOtherClockSource.setStatus(_A)
_CwnManualSource_ObjectIdentity=ObjectIdentity
cwnManualSource=_CwnManualSource_ObjectIdentity((1,3,6,1,4,1,9,9,223,1,3))
_CwnManualSourceTable_Object=MibTable
cwnManualSourceTable=_CwnManualSourceTable_Object((1,3,6,1,4,1,9,9,223,1,3,1))
if mibBuilder.loadTexts:cwnManualSourceTable.setStatus(_A)
_CwnManualSourceEntry_Object=MibTableRow
cwnManualSourceEntry=_CwnManualSourceEntry_Object((1,3,6,1,4,1,9,9,223,1,3,1,1))
cwnManualSourceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cwnManualSourceEntry.setStatus(_A)
class _CwnManualSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('default',3)))
_CwnManualSourcePriority_Type.__name__=_C
_CwnManualSourcePriority_Object=MibTableColumn
cwnManualSourcePriority=_CwnManualSourcePriority_Object((1,3,6,1,4,1,9,9,223,1,3,1,1,1),_CwnManualSourcePriority_Type())
cwnManualSourcePriority.setMaxAccess(_N)
if mibBuilder.loadTexts:cwnManualSourcePriority.setStatus(_A)
_CwnManualSourceIndex_Type=ClockSourceIndex
_CwnManualSourceIndex_Object=MibTableColumn
cwnManualSourceIndex=_CwnManualSourceIndex_Object((1,3,6,1,4,1,9,9,223,1,3,1,1,2),_CwnManualSourceIndex_Type())
cwnManualSourceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnManualSourceIndex.setStatus(_A)
_CwnManualClockHealth_Type=ClockHealthStatus
_CwnManualClockHealth_Object=MibTableColumn
cwnManualClockHealth=_CwnManualClockHealth_Object((1,3,6,1,4,1,9,9,223,1,3,1,1,3),_CwnManualClockHealth_Type())
cwnManualClockHealth.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnManualClockHealth.setStatus(_A)
_CwnManualRowStatus_Type=RowStatus
_CwnManualRowStatus_Object=MibTableColumn
cwnManualRowStatus=_CwnManualRowStatus_Object((1,3,6,1,4,1,9,9,223,1,3,1,1,4),_CwnManualRowStatus_Type())
cwnManualRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnManualRowStatus.setStatus(_A)
_CwnAtmSource_ObjectIdentity=ObjectIdentity
cwnAtmSource=_CwnAtmSource_ObjectIdentity((1,3,6,1,4,1,9,9,223,1,4))
_CwnAtmSourceTable_Object=MibTable
cwnAtmSourceTable=_CwnAtmSourceTable_Object((1,3,6,1,4,1,9,9,223,1,4,1))
if mibBuilder.loadTexts:cwnAtmSourceTable.setStatus(_A)
_CwnAtmSourceEntry_Object=MibTableRow
cwnAtmSourceEntry=_CwnAtmSourceEntry_Object((1,3,6,1,4,1,9,9,223,1,4,1,1))
cwnAtmSourceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwnAtmSourceEntry.setStatus(_A)
_CwnAtmSourceBestClockSource_Type=TruthValue
_CwnAtmSourceBestClockSource_Object=MibTableColumn
cwnAtmSourceBestClockSource=_CwnAtmSourceBestClockSource_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,1),_CwnAtmSourceBestClockSource_Type())
cwnAtmSourceBestClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnAtmSourceBestClockSource.setStatus(_A)
class _CwnAtmSourcePriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwnAtmSourcePriority_Type.__name__=_C
_CwnAtmSourcePriority_Object=MibTableColumn
cwnAtmSourcePriority=_CwnAtmSourcePriority_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,2),_CwnAtmSourcePriority_Type())
cwnAtmSourcePriority.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnAtmSourcePriority.setStatus(_A)
class _CwnAtmSourceStratum_Type(ClockStratum):defaultValue=4
_CwnAtmSourceStratum_Type.__name__=_G
_CwnAtmSourceStratum_Object=MibTableColumn
cwnAtmSourceStratum=_CwnAtmSourceStratum_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,3),_CwnAtmSourceStratum_Type())
cwnAtmSourceStratum.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnAtmSourceStratum.setStatus(_A)
class _CwnAtmSourcePRSReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_CwnAtmSourcePRSReference_Type.__name__=_C
_CwnAtmSourcePRSReference_Object=MibTableColumn
cwnAtmSourcePRSReference=_CwnAtmSourcePRSReference_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,4),_CwnAtmSourcePRSReference_Type())
cwnAtmSourcePRSReference.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnAtmSourcePRSReference.setStatus(_A)
_CwnAtmSourceClockHealth_Type=ClockHealthStatus
_CwnAtmSourceClockHealth_Object=MibTableColumn
cwnAtmSourceClockHealth=_CwnAtmSourceClockHealth_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,5),_CwnAtmSourceClockHealth_Type())
cwnAtmSourceClockHealth.setMaxAccess(_D)
if mibBuilder.loadTexts:cwnAtmSourceClockHealth.setStatus(_A)
_CwnAtmSourceRowStatus_Type=RowStatus
_CwnAtmSourceRowStatus_Object=MibTableColumn
cwnAtmSourceRowStatus=_CwnAtmSourceRowStatus_Object((1,3,6,1,4,1,9,9,223,1,4,1,1,6),_CwnAtmSourceRowStatus_Type())
cwnAtmSourceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwnAtmSourceRowStatus.setStatus(_A)
_CwnAtmInterface_ObjectIdentity=ObjectIdentity
cwnAtmInterface=_CwnAtmInterface_ObjectIdentity((1,3,6,1,4,1,9,9,223,1,5))
_CwnAtmInterfaceTable_Object=MibTable
cwnAtmInterfaceTable=_CwnAtmInterfaceTable_Object((1,3,6,1,4,1,9,9,223,1,5,1))
if mibBuilder.loadTexts:cwnAtmInterfaceTable.setStatus(_A)
_CwnAtmInterfaceEntry_Object=MibTableRow
cwnAtmInterfaceEntry=_CwnAtmInterfaceEntry_Object((1,3,6,1,4,1,9,9,223,1,5,1,1))
cwnAtmInterfaceEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cwnAtmInterfaceEntry.setStatus(_A)
class _CwnAtmInterfaceEnable_Type(TruthValue):defaultValue=1
_CwnAtmInterfaceEnable_Type.__name__=_L
_CwnAtmInterfaceEnable_Object=MibTableColumn
cwnAtmInterfaceEnable=_CwnAtmInterfaceEnable_Object((1,3,6,1,4,1,9,9,223,1,5,1,1,1),_CwnAtmInterfaceEnable_Type())
cwnAtmInterfaceEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnAtmInterfaceEnable.setStatus(_A)
class _CwnAtmInterfaceAdminWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_CwnAtmInterfaceAdminWeight_Type.__name__=_C
_CwnAtmInterfaceAdminWeight_Object=MibTableColumn
cwnAtmInterfaceAdminWeight=_CwnAtmInterfaceAdminWeight_Object((1,3,6,1,4,1,9,9,223,1,5,1,1,2),_CwnAtmInterfaceAdminWeight_Type())
cwnAtmInterfaceAdminWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnAtmInterfaceAdminWeight.setStatus(_A)
class _CwnAtmInterfaceVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwnAtmInterfaceVpi_Type.__name__=_C
_CwnAtmInterfaceVpi_Object=MibTableColumn
cwnAtmInterfaceVpi=_CwnAtmInterfaceVpi_Object((1,3,6,1,4,1,9,9,223,1,5,1,1,3),_CwnAtmInterfaceVpi_Type())
cwnAtmInterfaceVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnAtmInterfaceVpi.setStatus(_A)
class _CwnAtmInterfaceVci_Type(Integer32):defaultValue=34;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwnAtmInterfaceVci_Type.__name__=_C
_CwnAtmInterfaceVci_Object=MibTableColumn
cwnAtmInterfaceVci=_CwnAtmInterfaceVci_Object((1,3,6,1,4,1,9,9,223,1,5,1,1,4),_CwnAtmInterfaceVci_Type())
cwnAtmInterfaceVci.setMaxAccess(_E)
if mibBuilder.loadTexts:cwnAtmInterfaceVci.setStatus(_A)
_CiscoWanNcdpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoWanNcdpMIBNotificationPrefix=_CiscoWanNcdpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,223,2))
_CiscoWanNcdpMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoWanNcdpMIBNotifications=_CiscoWanNcdpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,223,2,0))
_CiscoWanNcdpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanNcdpMIBConformance=_CiscoWanNcdpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,223,3))
_CiscoWanNcdpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanNcdpMIBCompliances=_CiscoWanNcdpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,223,3,1))
_CiscoWanNcdpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanNcdpMIBGroups=_CiscoWanNcdpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,223,3,2))
ciscoWanNcdpGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,223,3,2,1))
ciscoWanNcdpGlobalGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoWanNcdpGlobalGroup.setStatus(_A)
ciscoWanNcdpClockSourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,223,3,2,2))
ciscoWanNcdpClockSourceGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoWanNcdpClockSourceGroup.setStatus(_A)
ciscoWanNcdpManualGroup=ObjectGroup((1,3,6,1,4,1,9,9,223,3,2,3))
ciscoWanNcdpManualGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoWanNcdpManualGroup.setStatus(_A)
ciscoWanNcdpAtmGroup=ObjectGroup((1,3,6,1,4,1,9,9,223,3,2,4))
ciscoWanNcdpAtmGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ciscoWanNcdpAtmGroup.setStatus(_A)
ciscoWanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,223,3,1,1))
ciscoWanMIBCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoWanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:ClockStratum,'ClockHealthStatus':ClockHealthStatus,'ClockSourceIndex':ClockSourceIndex,'ciscoWanNcdpMIB':ciscoWanNcdpMIB,'cwnMIBObjects':cwnMIBObjects,'cwnGlobal':cwnGlobal,_P:cwnDistributionMethod,_Q:cwnNodeStratum,_R:cwnMaxDiameter,_S:cwnMessageInterval,_T:cwnHoldTime,_U:cwnChangeReason,_V:cwnChangeTimeStamp,_W:cwnRootClockSource,'cwnClockSource':cwnClockSource,'cwnClockSourceTable':cwnClockSourceTable,'cwnClockSourceEntry':cwnClockSourceEntry,_H:cwnClockSourceIndex,_X:cwnClockSourceDesc,_Y:cwnInterfaceIndex,_Z:cwnOtherClockSource,'cwnManualSource':cwnManualSource,'cwnManualSourceTable':cwnManualSourceTable,'cwnManualSourceEntry':cwnManualSourceEntry,_O:cwnManualSourcePriority,_a:cwnManualSourceIndex,_b:cwnManualClockHealth,_c:cwnManualRowStatus,'cwnAtmSource':cwnAtmSource,'cwnAtmSourceTable':cwnAtmSourceTable,'cwnAtmSourceEntry':cwnAtmSourceEntry,_d:cwnAtmSourceBestClockSource,_e:cwnAtmSourcePriority,_f:cwnAtmSourceStratum,_g:cwnAtmSourcePRSReference,_h:cwnAtmSourceClockHealth,_i:cwnAtmSourceRowStatus,'cwnAtmInterface':cwnAtmInterface,'cwnAtmInterfaceTable':cwnAtmInterfaceTable,'cwnAtmInterfaceEntry':cwnAtmInterfaceEntry,_j:cwnAtmInterfaceEnable,_k:cwnAtmInterfaceAdminWeight,_l:cwnAtmInterfaceVpi,_m:cwnAtmInterfaceVci,'ciscoWanNcdpMIBNotificationPrefix':ciscoWanNcdpMIBNotificationPrefix,'ciscoWanNcdpMIBNotifications':ciscoWanNcdpMIBNotifications,'ciscoWanNcdpMIBConformance':ciscoWanNcdpMIBConformance,'ciscoWanNcdpMIBCompliances':ciscoWanNcdpMIBCompliances,'ciscoWanMIBCompliance':ciscoWanMIBCompliance,'ciscoWanNcdpMIBGroups':ciscoWanNcdpMIBGroups,_n:ciscoWanNcdpGlobalGroup,_o:ciscoWanNcdpClockSourceGroup,_p:ciscoWanNcdpManualGroup,_q:ciscoWanNcdpAtmGroup})