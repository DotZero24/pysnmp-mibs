_N='disabled'
_M='enabled'
_L='DisplayString'
_K='cienaCesLoopDetectionPortId'
_J='cienaCesLoopDetectionCfmServiceIndex'
_I='read-write'
_H='cienaCesLoopDetectionPortName'
_G='cienaGlobalSeverity'
_F='cienaGlobalMacAddress'
_E='read-only'
_D='Integer32'
_C='CIENA-GLOBAL-MIB'
_B='CIENA-CES-LOOP-DETECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_C,_F,_G)
cienaCesConfig,cienaCesNotifications,cienaCesStatistics=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications','cienaCesStatistics')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cienaCesLoopDetectionMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,50))
if mibBuilder.loadTexts:cienaCesLoopDetectionMIB.setRevisions(('2018-02-02 00:00',))
_CienaCesLoopDetectionMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBObjects=_CienaCesLoopDetectionMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,1))
_CienaCesLoopDetection_ObjectIdentity=ObjectIdentity
cienaCesLoopDetection=_CienaCesLoopDetection_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,1,1))
_CienaCesLoopDetectionAdminStatus_Type=CienaGlobalState
_CienaCesLoopDetectionAdminStatus_Object=MibScalar
cienaCesLoopDetectionAdminStatus=_CienaCesLoopDetectionAdminStatus_Object((1,3,6,1,4,1,1271,2,1,50,1,1,1),_CienaCesLoopDetectionAdminStatus_Type())
cienaCesLoopDetectionAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionAdminStatus.setStatus(_A)
_CienaCesLoopDetectionPortTable_Object=MibTable
cienaCesLoopDetectionPortTable=_CienaCesLoopDetectionPortTable_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortTable.setStatus(_A)
_CienaCesLoopDetectionPortEntry_Object=MibTableRow
cienaCesLoopDetectionPortEntry=_CienaCesLoopDetectionPortEntry_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1))
cienaCesLoopDetectionPortEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortEntry.setStatus(_A)
class _CienaCesLoopDetectionPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesLoopDetectionPortId_Type.__name__=_D
_CienaCesLoopDetectionPortId_Object=MibTableColumn
cienaCesLoopDetectionPortId=_CienaCesLoopDetectionPortId_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,1),_CienaCesLoopDetectionPortId_Type())
cienaCesLoopDetectionPortId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cienaCesLoopDetectionPortId.setStatus(_A)
class _CienaCesLoopDetectionPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CienaCesLoopDetectionPortName_Type.__name__=_L
_CienaCesLoopDetectionPortName_Object=MibTableColumn
cienaCesLoopDetectionPortName=_CienaCesLoopDetectionPortName_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,2),_CienaCesLoopDetectionPortName_Type())
cienaCesLoopDetectionPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortName.setStatus(_A)
class _CienaCesLoopDetectionPortAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CienaCesLoopDetectionPortAdminStatus_Type.__name__=_D
_CienaCesLoopDetectionPortAdminStatus_Object=MibTableColumn
cienaCesLoopDetectionPortAdminStatus=_CienaCesLoopDetectionPortAdminStatus_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,3),_CienaCesLoopDetectionPortAdminStatus_Type())
cienaCesLoopDetectionPortAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortAdminStatus.setStatus(_A)
class _CienaCesLoopDetectionPortAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('g8032',1),('portshut',2),('notify',3)))
_CienaCesLoopDetectionPortAction_Type.__name__=_D
_CienaCesLoopDetectionPortAction_Object=MibTableColumn
cienaCesLoopDetectionPortAction=_CienaCesLoopDetectionPortAction_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,4),_CienaCesLoopDetectionPortAction_Type())
cienaCesLoopDetectionPortAction.setMaxAccess(_I)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortAction.setStatus(_A)
class _CienaCesLoopDetectionPortRevertiveMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesLoopDetectionPortRevertiveMode_Type.__name__=_D
_CienaCesLoopDetectionPortRevertiveMode_Object=MibTableColumn
cienaCesLoopDetectionPortRevertiveMode=_CienaCesLoopDetectionPortRevertiveMode_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,5),_CienaCesLoopDetectionPortRevertiveMode_Type())
cienaCesLoopDetectionPortRevertiveMode.setMaxAccess(_I)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortRevertiveMode.setStatus(_A)
class _CienaCesLoopDetectionPortOperState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CienaCesLoopDetectionPortOperState_Type.__name__=_D
_CienaCesLoopDetectionPortOperState_Object=MibTableColumn
cienaCesLoopDetectionPortOperState=_CienaCesLoopDetectionPortOperState_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,6),_CienaCesLoopDetectionPortOperState_Type())
cienaCesLoopDetectionPortOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortOperState.setStatus(_A)
class _CienaCesLoopDetectionPortLoopStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_CienaCesLoopDetectionPortLoopStatus_Type.__name__=_D
_CienaCesLoopDetectionPortLoopStatus_Object=MibTableColumn
cienaCesLoopDetectionPortLoopStatus=_CienaCesLoopDetectionPortLoopStatus_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,7),_CienaCesLoopDetectionPortLoopStatus_Type())
cienaCesLoopDetectionPortLoopStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortLoopStatus.setStatus(_A)
_CienaCesLoopDetectionPortLoopOccurence_Type=Counter32
_CienaCesLoopDetectionPortLoopOccurence_Object=MibTableColumn
cienaCesLoopDetectionPortLoopOccurence=_CienaCesLoopDetectionPortLoopOccurence_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,8),_CienaCesLoopDetectionPortLoopOccurence_Type())
cienaCesLoopDetectionPortLoopOccurence.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionPortLoopOccurence.setStatus(_A)
class _CienaCesLoopDetectionHoldOffTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CienaCesLoopDetectionHoldOffTime_Type.__name__=_D
_CienaCesLoopDetectionHoldOffTime_Object=MibTableColumn
cienaCesLoopDetectionHoldOffTime=_CienaCesLoopDetectionHoldOffTime_Object((1,3,6,1,4,1,1271,2,1,50,1,1,2,1,9),_CienaCesLoopDetectionHoldOffTime_Type())
cienaCesLoopDetectionHoldOffTime.setMaxAccess(_I)
if mibBuilder.loadTexts:cienaCesLoopDetectionHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLoopDetectionHoldOffTime.setUnits('milliseconds')
_CienaCesLoopDetectionPortCfmServiceTable_Object=MibTable
cienaCesLoopDetectionPortCfmServiceTable=_CienaCesLoopDetectionPortCfmServiceTable_Object((1,3,6,1,4,1,1271,2,1,50,1,1,3))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortCfmServiceTable.setStatus(_A)
_CienaCesLoopDetectionPortCfmServiceEntry_Object=MibTableRow
cienaCesLoopDetectionPortCfmServiceEntry=_CienaCesLoopDetectionPortCfmServiceEntry_Object((1,3,6,1,4,1,1271,2,1,50,1,1,3,1))
cienaCesLoopDetectionPortCfmServiceEntry.setIndexNames((0,_B,_K),(0,_B,_J))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortCfmServiceEntry.setStatus(_A)
_CienaCesLoopDetectionCfmServiceIndex_Type=Unsigned32
_CienaCesLoopDetectionCfmServiceIndex_Object=MibTableColumn
cienaCesLoopDetectionCfmServiceIndex=_CienaCesLoopDetectionCfmServiceIndex_Object((1,3,6,1,4,1,1271,2,1,50,1,1,3,1,1),_CienaCesLoopDetectionCfmServiceIndex_Type())
cienaCesLoopDetectionCfmServiceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesLoopDetectionCfmServiceIndex.setStatus(_A)
_CienaCesLoopDetectionMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBNotificationPrefix=_CienaCesLoopDetectionMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,2))
_CienaCesLoopDetectionMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBNotifications=_CienaCesLoopDetectionMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,2,0))
_CienaCesLoopDetectionMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBConformance=_CienaCesLoopDetectionMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,3))
_CienaCesLoopDetectionMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBCompliances=_CienaCesLoopDetectionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,3,1))
_CienaCesLoopDetectionMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesLoopDetectionMIBGroups=_CienaCesLoopDetectionMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,50,3,2))
cienaCesLoopDetectionLoopFound=NotificationType((1,3,6,1,4,1,1271,2,1,50,2,0,1))
cienaCesLoopDetectionLoopFound.setObjects(*((_C,_G),(_C,_F),(_B,_J),(_B,_H)))
if mibBuilder.loadTexts:cienaCesLoopDetectionLoopFound.setStatus(_A)
cienaCesLoopDetectionLoopClear=NotificationType((1,3,6,1,4,1,1271,2,1,50,2,0,2))
cienaCesLoopDetectionLoopClear.setObjects(*((_C,_G),(_C,_F),(_B,_J),(_B,_H)))
if mibBuilder.loadTexts:cienaCesLoopDetectionLoopClear.setStatus(_A)
cienaCesLoopDetectionPortOperActionSet=NotificationType((1,3,6,1,4,1,1271,2,1,50,2,0,3))
cienaCesLoopDetectionPortOperActionSet.setObjects(*((_C,_G),(_C,_F),(_B,_H)))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortOperActionSet.setStatus(_A)
cienaCesLoopDetectionPortOperActionClear=NotificationType((1,3,6,1,4,1,1271,2,1,50,2,0,4))
cienaCesLoopDetectionPortOperActionClear.setObjects(*((_C,_G),(_C,_F),(_B,_H)))
if mibBuilder.loadTexts:cienaCesLoopDetectionPortOperActionClear.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaCesLoopDetectionMIB':cienaCesLoopDetectionMIB,'cienaCesLoopDetectionMIBObjects':cienaCesLoopDetectionMIBObjects,'cienaCesLoopDetection':cienaCesLoopDetection,'cienaCesLoopDetectionAdminStatus':cienaCesLoopDetectionAdminStatus,'cienaCesLoopDetectionPortTable':cienaCesLoopDetectionPortTable,'cienaCesLoopDetectionPortEntry':cienaCesLoopDetectionPortEntry,_K:cienaCesLoopDetectionPortId,_H:cienaCesLoopDetectionPortName,'cienaCesLoopDetectionPortAdminStatus':cienaCesLoopDetectionPortAdminStatus,'cienaCesLoopDetectionPortAction':cienaCesLoopDetectionPortAction,'cienaCesLoopDetectionPortRevertiveMode':cienaCesLoopDetectionPortRevertiveMode,'cienaCesLoopDetectionPortOperState':cienaCesLoopDetectionPortOperState,'cienaCesLoopDetectionPortLoopStatus':cienaCesLoopDetectionPortLoopStatus,'cienaCesLoopDetectionPortLoopOccurence':cienaCesLoopDetectionPortLoopOccurence,'cienaCesLoopDetectionHoldOffTime':cienaCesLoopDetectionHoldOffTime,'cienaCesLoopDetectionPortCfmServiceTable':cienaCesLoopDetectionPortCfmServiceTable,'cienaCesLoopDetectionPortCfmServiceEntry':cienaCesLoopDetectionPortCfmServiceEntry,_J:cienaCesLoopDetectionCfmServiceIndex,'cienaCesLoopDetectionMIBNotificationPrefix':cienaCesLoopDetectionMIBNotificationPrefix,'cienaCesLoopDetectionMIBNotifications':cienaCesLoopDetectionMIBNotifications,'cienaCesLoopDetectionLoopFound':cienaCesLoopDetectionLoopFound,'cienaCesLoopDetectionLoopClear':cienaCesLoopDetectionLoopClear,'cienaCesLoopDetectionPortOperActionSet':cienaCesLoopDetectionPortOperActionSet,'cienaCesLoopDetectionPortOperActionClear':cienaCesLoopDetectionPortOperActionClear,'cienaCesLoopDetectionMIBConformance':cienaCesLoopDetectionMIBConformance,'cienaCesLoopDetectionMIBCompliances':cienaCesLoopDetectionMIBCompliances,'cienaCesLoopDetectionMIBGroups':cienaCesLoopDetectionMIBGroups})