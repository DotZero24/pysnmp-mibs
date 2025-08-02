_l='cncNotificationGroup'
_k='cncGroup'
_j='cncNotifySourceChange'
_i='cncNcdpHealth'
_h='cncNcdpVci'
_g='cncNcdpVpi'
_f='cncNcdpAdminWeight'
_e='cncNcdpEnable'
_d='cncNcdpRowStatus'
_c='cncNcdpSourceHealth'
_b='cncNcdpPRSReference'
_a='cncNcdpStratum'
_Z='cncNcdpPriority'
_Y='cncNcdpBestClockSource'
_X='cncManualRowStatus'
_W='cncManualSourceHealth'
_V='cncManualSourceId'
_U='cncRootClockSource'
_T='cncSourceChangeTimeStamp'
_S='cncNcdpHoldTime'
_R='cncNcdpMessageInterval'
_Q='cncNcdpMaxDiameter'
_P='cncNodeStratum'
_O='cncNotificationOnChange'
_N='cncDistributionMethod'
_M='cncManualSourcePriority'
_L='milliseconds'
_K='TruthValue'
_J='TimeStamp'
_I='cncSourceChangeReason'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='read-create'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-ATM-NETWORK-CLOCK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_G,'PhysicalIndex',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J,_K)
ciscoAtmNetworkClockMIB=ModuleIdentity((1,3,6,1,4,1,9,9,121))
if mibBuilder.loadTexts:ciscoAtmNetworkClockMIB.setRevisions(('2008-02-18 00:00','2001-12-11 00:00'))
class CncStratum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('s1',1),('s2e',2),('s2',3),('s3e',4),('s3',5),('s4e',6),('s4',7),('other',8)))
class CncHealth(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('bad',2),('unknown',3)))
_CiscoAtmNetworkClockMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockMIBObjects=_CiscoAtmNetworkClockMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,121,1))
_CncGlobal_ObjectIdentity=ObjectIdentity
cncGlobal=_CncGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,121,1,1))
class _CncDistributionMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ncdp',1),('manual',2)))
_CncDistributionMethod_Type.__name__=_C
_CncDistributionMethod_Object=MibScalar
cncDistributionMethod=_CncDistributionMethod_Object((1,3,6,1,4,1,9,9,121,1,1,1),_CncDistributionMethod_Type())
cncDistributionMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cncDistributionMethod.setStatus(_A)
class _CncNotificationOnChange_Type(TruthValue):defaultValue=1
_CncNotificationOnChange_Type.__name__=_K
_CncNotificationOnChange_Object=MibScalar
cncNotificationOnChange=_CncNotificationOnChange_Object((1,3,6,1,4,1,9,9,121,1,1,2),_CncNotificationOnChange_Type())
cncNotificationOnChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNotificationOnChange.setStatus(_A)
_CncNodeStratum_Type=CncStratum
_CncNodeStratum_Object=MibScalar
cncNodeStratum=_CncNodeStratum_Object((1,3,6,1,4,1,9,9,121,1,1,3),_CncNodeStratum_Type())
cncNodeStratum.setMaxAccess(_E)
if mibBuilder.loadTexts:cncNodeStratum.setStatus(_A)
class _CncNcdpMaxDiameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_CncNcdpMaxDiameter_Type.__name__=_C
_CncNcdpMaxDiameter_Object=MibScalar
cncNcdpMaxDiameter=_CncNcdpMaxDiameter_Object((1,3,6,1,4,1,9,9,121,1,1,4),_CncNcdpMaxDiameter_Type())
cncNcdpMaxDiameter.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpMaxDiameter.setStatus(_A)
class _CncNcdpMessageInterval_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,60000))
_CncNcdpMessageInterval_Type.__name__=_C
_CncNcdpMessageInterval_Object=MibScalar
cncNcdpMessageInterval=_CncNcdpMessageInterval_Object((1,3,6,1,4,1,9,9,121,1,1,5),_CncNcdpMessageInterval_Type())
cncNcdpMessageInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpMessageInterval.setStatus(_A)
if mibBuilder.loadTexts:cncNcdpMessageInterval.setUnits(_L)
class _CncNcdpHoldTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,60000))
_CncNcdpHoldTime_Type.__name__=_C
_CncNcdpHoldTime_Object=MibScalar
cncNcdpHoldTime=_CncNcdpHoldTime_Object((1,3,6,1,4,1,9,9,121,1,1,6),_CncNcdpHoldTime_Type())
cncNcdpHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cncNcdpHoldTime.setUnits(_L)
class _CncSourceChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('lossOfLock',2),('lossOfActivity',3),('ncdpRestructure',4),('other',5)))
_CncSourceChangeReason_Type.__name__=_C
_CncSourceChangeReason_Object=MibScalar
cncSourceChangeReason=_CncSourceChangeReason_Object((1,3,6,1,4,1,9,9,121,1,1,7),_CncSourceChangeReason_Type())
cncSourceChangeReason.setMaxAccess(_E)
if mibBuilder.loadTexts:cncSourceChangeReason.setStatus(_A)
class _CncSourceChangeTimeStamp_Type(TimeStamp):defaultValue=0
_CncSourceChangeTimeStamp_Type.__name__=_J
_CncSourceChangeTimeStamp_Object=MibScalar
cncSourceChangeTimeStamp=_CncSourceChangeTimeStamp_Object((1,3,6,1,4,1,9,9,121,1,1,8),_CncSourceChangeTimeStamp_Type())
cncSourceChangeTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:cncSourceChangeTimeStamp.setStatus(_A)
_CncRootClockSource_Type=PhysicalIndex
_CncRootClockSource_Object=MibScalar
cncRootClockSource=_CncRootClockSource_Object((1,3,6,1,4,1,9,9,121,1,1,9),_CncRootClockSource_Type())
cncRootClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:cncRootClockSource.setStatus(_A)
_CncManualSource_ObjectIdentity=ObjectIdentity
cncManualSource=_CncManualSource_ObjectIdentity((1,3,6,1,4,1,9,9,121,1,2))
_CncManualSourceTable_Object=MibTable
cncManualSourceTable=_CncManualSourceTable_Object((1,3,6,1,4,1,9,9,121,1,2,1))
if mibBuilder.loadTexts:cncManualSourceTable.setStatus(_A)
_CncManualSourceEntry_Object=MibTableRow
cncManualSourceEntry=_CncManualSourceEntry_Object((1,3,6,1,4,1,9,9,121,1,2,1,1))
cncManualSourceEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cncManualSourceEntry.setStatus(_A)
class _CncManualSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('default',3)))
_CncManualSourcePriority_Type.__name__=_C
_CncManualSourcePriority_Object=MibTableColumn
cncManualSourcePriority=_CncManualSourcePriority_Object((1,3,6,1,4,1,9,9,121,1,2,1,1,1),_CncManualSourcePriority_Type())
cncManualSourcePriority.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cncManualSourcePriority.setStatus(_A)
_CncManualSourceId_Type=PhysicalIndex
_CncManualSourceId_Object=MibTableColumn
cncManualSourceId=_CncManualSourceId_Object((1,3,6,1,4,1,9,9,121,1,2,1,1,2),_CncManualSourceId_Type())
cncManualSourceId.setMaxAccess(_F)
if mibBuilder.loadTexts:cncManualSourceId.setStatus(_A)
_CncManualSourceHealth_Type=CncHealth
_CncManualSourceHealth_Object=MibTableColumn
cncManualSourceHealth=_CncManualSourceHealth_Object((1,3,6,1,4,1,9,9,121,1,2,1,1,3),_CncManualSourceHealth_Type())
cncManualSourceHealth.setMaxAccess(_E)
if mibBuilder.loadTexts:cncManualSourceHealth.setStatus(_A)
_CncManualRowStatus_Type=RowStatus
_CncManualRowStatus_Object=MibTableColumn
cncManualRowStatus=_CncManualRowStatus_Object((1,3,6,1,4,1,9,9,121,1,2,1,1,4),_CncManualRowStatus_Type())
cncManualRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cncManualRowStatus.setStatus(_A)
_CncNcdpSource_ObjectIdentity=ObjectIdentity
cncNcdpSource=_CncNcdpSource_ObjectIdentity((1,3,6,1,4,1,9,9,121,1,3))
_CncNcdpSourceTable_Object=MibTable
cncNcdpSourceTable=_CncNcdpSourceTable_Object((1,3,6,1,4,1,9,9,121,1,3,1))
if mibBuilder.loadTexts:cncNcdpSourceTable.setStatus(_A)
_CncNcdpSourceEntry_Object=MibTableRow
cncNcdpSourceEntry=_CncNcdpSourceEntry_Object((1,3,6,1,4,1,9,9,121,1,3,1,1))
cncNcdpSourceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cncNcdpSourceEntry.setStatus(_A)
_CncNcdpBestClockSource_Type=TruthValue
_CncNcdpBestClockSource_Object=MibTableColumn
cncNcdpBestClockSource=_CncNcdpBestClockSource_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,1),_CncNcdpBestClockSource_Type())
cncNcdpBestClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:cncNcdpBestClockSource.setStatus(_A)
class _CncNcdpPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CncNcdpPriority_Type.__name__=_C
_CncNcdpPriority_Object=MibTableColumn
cncNcdpPriority=_CncNcdpPriority_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,2),_CncNcdpPriority_Type())
cncNcdpPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:cncNcdpPriority.setStatus(_A)
_CncNcdpStratum_Type=CncStratum
_CncNcdpStratum_Object=MibTableColumn
cncNcdpStratum=_CncNcdpStratum_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,3),_CncNcdpStratum_Type())
cncNcdpStratum.setMaxAccess(_F)
if mibBuilder.loadTexts:cncNcdpStratum.setStatus(_A)
class _CncNcdpPRSReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_CncNcdpPRSReference_Type.__name__=_C
_CncNcdpPRSReference_Object=MibTableColumn
cncNcdpPRSReference=_CncNcdpPRSReference_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,4),_CncNcdpPRSReference_Type())
cncNcdpPRSReference.setMaxAccess(_F)
if mibBuilder.loadTexts:cncNcdpPRSReference.setStatus(_A)
_CncNcdpSourceHealth_Type=CncHealth
_CncNcdpSourceHealth_Object=MibTableColumn
cncNcdpSourceHealth=_CncNcdpSourceHealth_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,5),_CncNcdpSourceHealth_Type())
cncNcdpSourceHealth.setMaxAccess(_E)
if mibBuilder.loadTexts:cncNcdpSourceHealth.setStatus(_A)
_CncNcdpRowStatus_Type=RowStatus
_CncNcdpRowStatus_Object=MibTableColumn
cncNcdpRowStatus=_CncNcdpRowStatus_Object((1,3,6,1,4,1,9,9,121,1,3,1,1,6),_CncNcdpRowStatus_Type())
cncNcdpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cncNcdpRowStatus.setStatus(_A)
_CncNcdp_ObjectIdentity=ObjectIdentity
cncNcdp=_CncNcdp_ObjectIdentity((1,3,6,1,4,1,9,9,121,1,4))
_CncNcdpAtmTable_Object=MibTable
cncNcdpAtmTable=_CncNcdpAtmTable_Object((1,3,6,1,4,1,9,9,121,1,4,1))
if mibBuilder.loadTexts:cncNcdpAtmTable.setStatus(_A)
_CncNcdpAtmEntry_Object=MibTableRow
cncNcdpAtmEntry=_CncNcdpAtmEntry_Object((1,3,6,1,4,1,9,9,121,1,4,1,1))
cncNcdpAtmEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cncNcdpAtmEntry.setStatus(_A)
_CncNcdpEnable_Type=TruthValue
_CncNcdpEnable_Object=MibTableColumn
cncNcdpEnable=_CncNcdpEnable_Object((1,3,6,1,4,1,9,9,121,1,4,1,1,1),_CncNcdpEnable_Type())
cncNcdpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpEnable.setStatus(_A)
class _CncNcdpAdminWeight_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_CncNcdpAdminWeight_Type.__name__=_C
_CncNcdpAdminWeight_Object=MibTableColumn
cncNcdpAdminWeight=_CncNcdpAdminWeight_Object((1,3,6,1,4,1,9,9,121,1,4,1,1,2),_CncNcdpAdminWeight_Type())
cncNcdpAdminWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpAdminWeight.setStatus(_A)
class _CncNcdpVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CncNcdpVpi_Type.__name__=_C
_CncNcdpVpi_Object=MibTableColumn
cncNcdpVpi=_CncNcdpVpi_Object((1,3,6,1,4,1,9,9,121,1,4,1,1,3),_CncNcdpVpi_Type())
cncNcdpVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpVpi.setStatus(_A)
class _CncNcdpVci_Type(Integer32):defaultValue=34;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CncNcdpVci_Type.__name__=_C
_CncNcdpVci_Object=MibTableColumn
cncNcdpVci=_CncNcdpVci_Object((1,3,6,1,4,1,9,9,121,1,4,1,1,4),_CncNcdpVci_Type())
cncNcdpVci.setMaxAccess(_D)
if mibBuilder.loadTexts:cncNcdpVci.setStatus(_A)
_CncNcdpHealth_Type=CncHealth
_CncNcdpHealth_Object=MibTableColumn
cncNcdpHealth=_CncNcdpHealth_Object((1,3,6,1,4,1,9,9,121,1,4,1,1,5),_CncNcdpHealth_Type())
cncNcdpHealth.setMaxAccess(_E)
if mibBuilder.loadTexts:cncNcdpHealth.setStatus(_A)
_CiscoAtmNetworkClockNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockNotificationPrefix=_CiscoAtmNetworkClockNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,121,2))
_CiscoAtmNetworkClockMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockMIBNotifications=_CiscoAtmNetworkClockMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,121,2,0))
_CiscoAtmNetworkClockConformance_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockConformance=_CiscoAtmNetworkClockConformance_ObjectIdentity((1,3,6,1,4,1,9,9,121,3))
_CiscoAtmNetworkClockMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockMIBCompliances=_CiscoAtmNetworkClockMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,121,3,1))
_CiscoAtmNetworkClockMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmNetworkClockMIBGroups=_CiscoAtmNetworkClockMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,121,3,2))
cncGroup=ObjectGroup((1,3,6,1,4,1,9,9,121,3,2,1))
cncGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cncGroup.setStatus(_A)
cncNotifySourceChange=NotificationType((1,3,6,1,4,1,9,9,121,2,0,1))
cncNotifySourceChange.setObjects((_B,_I))
if mibBuilder.loadTexts:cncNotifySourceChange.setStatus(_A)
cncNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,121,3,2,2))
cncNotificationGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:cncNotificationGroup.setStatus(_A)
cncMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,121,3,1,1))
cncMIBCompliance.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cncMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CncStratum':CncStratum,'CncHealth':CncHealth,'ciscoAtmNetworkClockMIB':ciscoAtmNetworkClockMIB,'ciscoAtmNetworkClockMIBObjects':ciscoAtmNetworkClockMIBObjects,'cncGlobal':cncGlobal,_N:cncDistributionMethod,_O:cncNotificationOnChange,_P:cncNodeStratum,_Q:cncNcdpMaxDiameter,_R:cncNcdpMessageInterval,_S:cncNcdpHoldTime,_I:cncSourceChangeReason,_T:cncSourceChangeTimeStamp,_U:cncRootClockSource,'cncManualSource':cncManualSource,'cncManualSourceTable':cncManualSourceTable,'cncManualSourceEntry':cncManualSourceEntry,_M:cncManualSourcePriority,_V:cncManualSourceId,_W:cncManualSourceHealth,_X:cncManualRowStatus,'cncNcdpSource':cncNcdpSource,'cncNcdpSourceTable':cncNcdpSourceTable,'cncNcdpSourceEntry':cncNcdpSourceEntry,_Y:cncNcdpBestClockSource,_Z:cncNcdpPriority,_a:cncNcdpStratum,_b:cncNcdpPRSReference,_c:cncNcdpSourceHealth,_d:cncNcdpRowStatus,'cncNcdp':cncNcdp,'cncNcdpAtmTable':cncNcdpAtmTable,'cncNcdpAtmEntry':cncNcdpAtmEntry,_e:cncNcdpEnable,_f:cncNcdpAdminWeight,_g:cncNcdpVpi,_h:cncNcdpVci,_i:cncNcdpHealth,'ciscoAtmNetworkClockNotificationPrefix':ciscoAtmNetworkClockNotificationPrefix,'ciscoAtmNetworkClockMIBNotifications':ciscoAtmNetworkClockMIBNotifications,_j:cncNotifySourceChange,'ciscoAtmNetworkClockConformance':ciscoAtmNetworkClockConformance,'ciscoAtmNetworkClockMIBCompliances':ciscoAtmNetworkClockMIBCompliances,'cncMIBCompliance':cncMIBCompliance,'ciscoAtmNetworkClockMIBGroups':ciscoAtmNetworkClockMIBGroups,_k:cncGroup,_l:cncNotificationGroup})