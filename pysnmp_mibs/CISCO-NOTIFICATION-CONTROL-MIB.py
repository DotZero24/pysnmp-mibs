_V='cNotifCtrlConfigExtGroup'
_U='cNotifCtrlDescr'
_T='cNotifCtrlRowStatus'
_S='cNotifCtrlStorageType'
_R='cNotifCtrlOID'
_Q='cNotifCtrlIndexNext'
_P='cNotifCtrlTableSize'
_O='cNotifCtrlSamplingInterval'
_N='cNotifCtrlThreshold'
_M='cNotifCtrlCurrentState'
_L='cNotifCtrlMode'
_K='cNotifCtrlIndex'
_J='read-only'
_I='StorageType'
_H='SnmpAdminString'
_G='cNotifCtrlConfigGroup'
_F='Integer32'
_E='read-create'
_D='read-write'
_C='Unsigned32'
_B='CISCO-NOTIFICATION-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention')
ciscoNotificationControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,586))
if mibBuilder.loadTexts:ciscoNotificationControlMIB.setRevisions(('2009-09-20 00:00','2006-09-27 00:00'))
_CNotifCtrlMIBObjects_ObjectIdentity=ObjectIdentity
cNotifCtrlMIBObjects=_CNotifCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,586,1))
_CNotifCtrlConfig_ObjectIdentity=ObjectIdentity
cNotifCtrlConfig=_CNotifCtrlConfig_ObjectIdentity((1,3,6,1,4,1,9,9,586,1,1))
class _CNotifCtrlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noControl',1),('forcedControl',2),('automaticControl',3)))
_CNotifCtrlMode_Type.__name__=_F
_CNotifCtrlMode_Object=MibScalar
cNotifCtrlMode=_CNotifCtrlMode_Object((1,3,6,1,4,1,9,9,586,1,1,1),_CNotifCtrlMode_Type())
cNotifCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cNotifCtrlMode.setStatus(_A)
class _CNotifCtrlCurrentState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlOn',1),('controlOff',2)))
_CNotifCtrlCurrentState_Type.__name__=_F
_CNotifCtrlCurrentState_Object=MibScalar
cNotifCtrlCurrentState=_CNotifCtrlCurrentState_Object((1,3,6,1,4,1,9,9,586,1,1,2),_CNotifCtrlCurrentState_Type())
cNotifCtrlCurrentState.setMaxAccess(_J)
if mibBuilder.loadTexts:cNotifCtrlCurrentState.setStatus(_A)
class _CNotifCtrlThreshold_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CNotifCtrlThreshold_Type.__name__=_C
_CNotifCtrlThreshold_Object=MibScalar
cNotifCtrlThreshold=_CNotifCtrlThreshold_Object((1,3,6,1,4,1,9,9,586,1,1,3),_CNotifCtrlThreshold_Type())
cNotifCtrlThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cNotifCtrlThreshold.setStatus(_A)
if mibBuilder.loadTexts:cNotifCtrlThreshold.setUnits('notifications')
class _CNotifCtrlSamplingInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CNotifCtrlSamplingInterval_Type.__name__=_C
_CNotifCtrlSamplingInterval_Object=MibScalar
cNotifCtrlSamplingInterval=_CNotifCtrlSamplingInterval_Object((1,3,6,1,4,1,9,9,586,1,1,4),_CNotifCtrlSamplingInterval_Type())
cNotifCtrlSamplingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cNotifCtrlSamplingInterval.setStatus(_A)
if mibBuilder.loadTexts:cNotifCtrlSamplingInterval.setUnits('minutes')
class _CNotifCtrlTableSize_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CNotifCtrlTableSize_Type.__name__=_C
_CNotifCtrlTableSize_Object=MibScalar
cNotifCtrlTableSize=_CNotifCtrlTableSize_Object((1,3,6,1,4,1,9,9,586,1,1,5),_CNotifCtrlTableSize_Type())
cNotifCtrlTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cNotifCtrlTableSize.setStatus(_A)
class _CNotifCtrlIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CNotifCtrlIndexNext_Type.__name__=_C
_CNotifCtrlIndexNext_Object=MibScalar
cNotifCtrlIndexNext=_CNotifCtrlIndexNext_Object((1,3,6,1,4,1,9,9,586,1,1,6),_CNotifCtrlIndexNext_Type())
cNotifCtrlIndexNext.setMaxAccess(_J)
if mibBuilder.loadTexts:cNotifCtrlIndexNext.setStatus(_A)
_CNotifCtrlTable_Object=MibTable
cNotifCtrlTable=_CNotifCtrlTable_Object((1,3,6,1,4,1,9,9,586,1,1,7))
if mibBuilder.loadTexts:cNotifCtrlTable.setStatus(_A)
_CNotifCtrlEntry_Object=MibTableRow
cNotifCtrlEntry=_CNotifCtrlEntry_Object((1,3,6,1,4,1,9,9,586,1,1,7,1))
cNotifCtrlEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cNotifCtrlEntry.setStatus(_A)
class _CNotifCtrlIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CNotifCtrlIndex_Type.__name__=_C
_CNotifCtrlIndex_Object=MibTableColumn
cNotifCtrlIndex=_CNotifCtrlIndex_Object((1,3,6,1,4,1,9,9,586,1,1,7,1,1),_CNotifCtrlIndex_Type())
cNotifCtrlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cNotifCtrlIndex.setStatus(_A)
_CNotifCtrlOID_Type=AutonomousType
_CNotifCtrlOID_Object=MibTableColumn
cNotifCtrlOID=_CNotifCtrlOID_Object((1,3,6,1,4,1,9,9,586,1,1,7,1,2),_CNotifCtrlOID_Type())
cNotifCtrlOID.setMaxAccess(_E)
if mibBuilder.loadTexts:cNotifCtrlOID.setStatus(_A)
class _CNotifCtrlStorageType_Type(StorageType):defaultValue=3
_CNotifCtrlStorageType_Type.__name__=_I
_CNotifCtrlStorageType_Object=MibTableColumn
cNotifCtrlStorageType=_CNotifCtrlStorageType_Object((1,3,6,1,4,1,9,9,586,1,1,7,1,3),_CNotifCtrlStorageType_Type())
cNotifCtrlStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cNotifCtrlStorageType.setStatus(_A)
_CNotifCtrlRowStatus_Type=RowStatus
_CNotifCtrlRowStatus_Object=MibTableColumn
cNotifCtrlRowStatus=_CNotifCtrlRowStatus_Object((1,3,6,1,4,1,9,9,586,1,1,7,1,4),_CNotifCtrlRowStatus_Type())
cNotifCtrlRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cNotifCtrlRowStatus.setStatus(_A)
class _CNotifCtrlDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CNotifCtrlDescr_Type.__name__=_H
_CNotifCtrlDescr_Object=MibTableColumn
cNotifCtrlDescr=_CNotifCtrlDescr_Object((1,3,6,1,4,1,9,9,586,1,1,7,1,5),_CNotifCtrlDescr_Type())
cNotifCtrlDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:cNotifCtrlDescr.setStatus(_A)
_CNotifCtrlMIBConformance_ObjectIdentity=ObjectIdentity
cNotifCtrlMIBConformance=_CNotifCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,586,2))
_CNotifCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
cNotifCtrlMIBCompliances=_CNotifCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,586,2,1))
_CNotifCtrlMIBGroups_ObjectIdentity=ObjectIdentity
cNotifCtrlMIBGroups=_CNotifCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,586,2,2))
cNotifCtrlConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,586,2,2,1))
cNotifCtrlConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cNotifCtrlConfigGroup.setStatus(_A)
cNotifCtrlConfigExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,586,2,2,2))
cNotifCtrlConfigExtGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:cNotifCtrlConfigExtGroup.setStatus(_A)
cNotifCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,586,2,1,1))
cNotifCtrlMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:cNotifCtrlMIBCompliance.setStatus('deprecated')
cNotifCtrlMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,586,2,1,2))
cNotifCtrlMIBComplianceRev1.setObjects(*((_B,_G),(_B,_V)))
if mibBuilder.loadTexts:cNotifCtrlMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNotificationControlMIB':ciscoNotificationControlMIB,'cNotifCtrlMIBObjects':cNotifCtrlMIBObjects,'cNotifCtrlConfig':cNotifCtrlConfig,_L:cNotifCtrlMode,_M:cNotifCtrlCurrentState,_N:cNotifCtrlThreshold,_O:cNotifCtrlSamplingInterval,_P:cNotifCtrlTableSize,_Q:cNotifCtrlIndexNext,'cNotifCtrlTable':cNotifCtrlTable,'cNotifCtrlEntry':cNotifCtrlEntry,_K:cNotifCtrlIndex,_R:cNotifCtrlOID,_S:cNotifCtrlStorageType,_T:cNotifCtrlRowStatus,_U:cNotifCtrlDescr,'cNotifCtrlMIBConformance':cNotifCtrlMIBConformance,'cNotifCtrlMIBCompliances':cNotifCtrlMIBCompliances,'cNotifCtrlMIBCompliance':cNotifCtrlMIBCompliance,'cNotifCtrlMIBComplianceRev1':cNotifCtrlMIBComplianceRev1,'cNotifCtrlMIBGroups':cNotifCtrlMIBGroups,_G:cNotifCtrlConfigGroup,_V:cNotifCtrlConfigExtGroup})