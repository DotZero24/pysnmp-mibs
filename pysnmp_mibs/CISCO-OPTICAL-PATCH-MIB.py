_e='cOPatchGroup1'
_d='cOPatchIntfGroup'
_c='cOPatchGroup'
_b='cOPatchInterfaceGroup'
_a='cOPatchEvent'
_Z='cOPatchDirOnLowIf'
_Y='cOPatchIntfPatchId'
_X='cOPatchIdentifier'
_W='cOPatchIntfDirection'
_V='not-accessible'
_U='cOPatchIndex'
_T='TruthValue'
_S='cOPatchNotifyGroup'
_R='cOPatchRowStatus'
_Q='cOPatchCreationTime'
_P='cOPatchEventEnabled'
_O='cOPatchLastChange'
_N='cOPatchIndexNext'
_M='ifIndex'
_L='IF-MIB'
_K='cOPatchStatus'
_J='cOPatchType'
_I='cOPatchHighIfIndex'
_H='cOPatchLowIfIndex'
_G='cOPatchEventType'
_F='read-create'
_E='deprecated'
_D='read-only'
_C='Integer32'
_B='current'
_A='CISCO-OPTICAL-PATCH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_L,'InterfaceIndex',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_T)
ciscoOpticalPatchMIB=ModuleIdentity((1,3,6,1,4,1,9,10,67))
if mibBuilder.loadTexts:ciscoOpticalPatchMIB.setRevisions(('2002-03-18 00:00','2001-09-05 00:00'))
_COPatchMIBObjects_ObjectIdentity=ObjectIdentity
cOPatchMIBObjects=_COPatchMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,67,1))
_COPatchInterfaceTable_Object=MibTable
cOPatchInterfaceTable=_COPatchInterfaceTable_Object((1,3,6,1,4,1,9,10,67,1,1))
if mibBuilder.loadTexts:cOPatchInterfaceTable.setStatus(_E)
_COPatchInterfaceEntry_Object=MibTableRow
cOPatchInterfaceEntry=_COPatchInterfaceEntry_Object((1,3,6,1,4,1,9,10,67,1,1,1))
cOPatchInterfaceEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:cOPatchInterfaceEntry.setStatus(_E)
class _COPatchIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483547))
_COPatchIdentifier_Type.__name__=_C
_COPatchIdentifier_Object=MibTableColumn
cOPatchIdentifier=_COPatchIdentifier_Object((1,3,6,1,4,1,9,10,67,1,1,1,1),_COPatchIdentifier_Type())
cOPatchIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchIdentifier.setStatus(_E)
class _COPatchIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_COPatchIndexNext_Type.__name__=_C
_COPatchIndexNext_Object=MibScalar
cOPatchIndexNext=_COPatchIndexNext_Object((1,3,6,1,4,1,9,10,67,1,2),_COPatchIndexNext_Type())
cOPatchIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchIndexNext.setStatus(_B)
_COPatchLastChange_Type=TimeStamp
_COPatchLastChange_Object=MibScalar
cOPatchLastChange=_COPatchLastChange_Object((1,3,6,1,4,1,9,10,67,1,3),_COPatchLastChange_Type())
cOPatchLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchLastChange.setStatus(_B)
class _COPatchEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('create',1),('delete',2),('modify',3)))
_COPatchEventType_Type.__name__=_C
_COPatchEventType_Object=MibScalar
cOPatchEventType=_COPatchEventType_Object((1,3,6,1,4,1,9,10,67,1,4),_COPatchEventType_Type())
cOPatchEventType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchEventType.setStatus(_B)
_COPatchTable_Object=MibTable
cOPatchTable=_COPatchTable_Object((1,3,6,1,4,1,9,10,67,1,5))
if mibBuilder.loadTexts:cOPatchTable.setStatus(_B)
_COPatchEntry_Object=MibTableRow
cOPatchEntry=_COPatchEntry_Object((1,3,6,1,4,1,9,10,67,1,5,1))
cOPatchEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:cOPatchEntry.setStatus(_B)
class _COPatchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_COPatchIndex_Type.__name__=_C
_COPatchIndex_Object=MibTableColumn
cOPatchIndex=_COPatchIndex_Object((1,3,6,1,4,1,9,10,67,1,5,1,1),_COPatchIndex_Type())
cOPatchIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:cOPatchIndex.setStatus(_B)
_COPatchLowIfIndex_Type=InterfaceIndex
_COPatchLowIfIndex_Object=MibTableColumn
cOPatchLowIfIndex=_COPatchLowIfIndex_Object((1,3,6,1,4,1,9,10,67,1,5,1,2),_COPatchLowIfIndex_Type())
cOPatchLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cOPatchLowIfIndex.setStatus(_B)
_COPatchHighIfIndex_Type=InterfaceIndex
_COPatchHighIfIndex_Object=MibTableColumn
cOPatchHighIfIndex=_COPatchHighIfIndex_Object((1,3,6,1,4,1,9,10,67,1,5,1,3),_COPatchHighIfIndex_Type())
cOPatchHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cOPatchHighIfIndex.setStatus(_B)
class _COPatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('provisioned',1),('automatic',2),('other',3)))
_COPatchType_Type.__name__=_C
_COPatchType_Object=MibTableColumn
cOPatchType=_COPatchType_Object((1,3,6,1,4,1,9,10,67,1,5,1,4),_COPatchType_Type())
cOPatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchType.setStatus(_B)
class _COPatchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noError',1),('otherError',2),('interfaceError',3),('interfaceChannelError',4)))
_COPatchStatus_Type.__name__=_C
_COPatchStatus_Object=MibTableColumn
cOPatchStatus=_COPatchStatus_Object((1,3,6,1,4,1,9,10,67,1,5,1,5),_COPatchStatus_Type())
cOPatchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchStatus.setStatus(_B)
_COPatchCreationTime_Type=TimeStamp
_COPatchCreationTime_Object=MibTableColumn
cOPatchCreationTime=_COPatchCreationTime_Object((1,3,6,1,4,1,9,10,67,1,5,1,6),_COPatchCreationTime_Type())
cOPatchCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchCreationTime.setStatus(_B)
_COPatchRowStatus_Type=RowStatus
_COPatchRowStatus_Object=MibTableColumn
cOPatchRowStatus=_COPatchRowStatus_Object((1,3,6,1,4,1,9,10,67,1,5,1,7),_COPatchRowStatus_Type())
cOPatchRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cOPatchRowStatus.setStatus(_B)
class _COPatchDirOnLowIf_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lowIfDirReceive',1),('lowIfDirTransmit',2),('lowIfDirBoth',3)))
_COPatchDirOnLowIf_Type.__name__=_C
_COPatchDirOnLowIf_Object=MibTableColumn
cOPatchDirOnLowIf=_COPatchDirOnLowIf_Object((1,3,6,1,4,1,9,10,67,1,5,1,8),_COPatchDirOnLowIf_Type())
cOPatchDirOnLowIf.setMaxAccess(_F)
if mibBuilder.loadTexts:cOPatchDirOnLowIf.setStatus(_B)
class _COPatchEventEnabled_Type(TruthValue):defaultValue=2
_COPatchEventEnabled_Type.__name__=_T
_COPatchEventEnabled_Object=MibScalar
cOPatchEventEnabled=_COPatchEventEnabled_Object((1,3,6,1,4,1,9,10,67,1,6),_COPatchEventEnabled_Type())
cOPatchEventEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:cOPatchEventEnabled.setStatus(_B)
_COPatchIntfTable_Object=MibTable
cOPatchIntfTable=_COPatchIntfTable_Object((1,3,6,1,4,1,9,10,67,1,7))
if mibBuilder.loadTexts:cOPatchIntfTable.setStatus(_B)
_COPatchIntfEntry_Object=MibTableRow
cOPatchIntfEntry=_COPatchIntfEntry_Object((1,3,6,1,4,1,9,10,67,1,7,1))
cOPatchIntfEntry.setIndexNames((0,_L,_M),(0,_A,_W))
if mibBuilder.loadTexts:cOPatchIntfEntry.setStatus(_B)
class _COPatchIntfDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receive',1),('transmit',2),('both',3)))
_COPatchIntfDirection_Type.__name__=_C
_COPatchIntfDirection_Object=MibTableColumn
cOPatchIntfDirection=_COPatchIntfDirection_Object((1,3,6,1,4,1,9,10,67,1,7,1,1),_COPatchIntfDirection_Type())
cOPatchIntfDirection.setMaxAccess(_V)
if mibBuilder.loadTexts:cOPatchIntfDirection.setStatus(_B)
class _COPatchIntfPatchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483547))
_COPatchIntfPatchId_Type.__name__=_C
_COPatchIntfPatchId_Object=MibTableColumn
cOPatchIntfPatchId=_COPatchIntfPatchId_Object((1,3,6,1,4,1,9,10,67,1,7,1,2),_COPatchIntfPatchId_Type())
cOPatchIntfPatchId.setMaxAccess(_D)
if mibBuilder.loadTexts:cOPatchIntfPatchId.setStatus(_B)
_COPatchMIBNotifications_ObjectIdentity=ObjectIdentity
cOPatchMIBNotifications=_COPatchMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,67,2))
_COPatchMIBConformance_ObjectIdentity=ObjectIdentity
cOPatchMIBConformance=_COPatchMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,67,3))
_COPatchMIBCompliances_ObjectIdentity=ObjectIdentity
cOPatchMIBCompliances=_COPatchMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,67,3,1))
_COPatchMIBGroups_ObjectIdentity=ObjectIdentity
cOPatchMIBGroups=_COPatchMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,67,3,2))
cOPatchInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,10,67,3,2,1))
cOPatchInterfaceGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:cOPatchInterfaceGroup.setStatus(_E)
cOPatchGroup=ObjectGroup((1,3,6,1,4,1,9,10,67,3,2,2))
cOPatchGroup.setObjects(*((_A,_N),(_A,_O),(_A,_G),(_A,_P),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cOPatchGroup.setStatus(_E)
cOPatchIntfGroup=ObjectGroup((1,3,6,1,4,1,9,10,67,3,2,4))
cOPatchIntfGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:cOPatchIntfGroup.setStatus(_B)
cOPatchGroup1=ObjectGroup((1,3,6,1,4,1,9,10,67,3,2,5))
cOPatchGroup1.setObjects(*((_A,_N),(_A,_O),(_A,_G),(_A,_P),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_Z)))
if mibBuilder.loadTexts:cOPatchGroup1.setStatus(_B)
cOPatchEvent=NotificationType((1,3,6,1,4,1,9,10,67,2,1))
cOPatchEvent.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_G)))
if mibBuilder.loadTexts:cOPatchEvent.setStatus(_B)
cOPatchNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,10,67,3,2,3))
cOPatchNotifyGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:cOPatchNotifyGroup.setStatus(_B)
cOPatchMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,67,3,1,1))
cOPatchMIBCompliance.setObjects(*((_A,_b),(_A,_c),(_A,_S)))
if mibBuilder.loadTexts:cOPatchMIBCompliance.setStatus(_E)
cOPatchMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,10,67,3,1,2))
cOPatchMIBCompliance1.setObjects(*((_A,_d),(_A,_e),(_A,_S)))
if mibBuilder.loadTexts:cOPatchMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoOpticalPatchMIB':ciscoOpticalPatchMIB,'cOPatchMIBObjects':cOPatchMIBObjects,'cOPatchInterfaceTable':cOPatchInterfaceTable,'cOPatchInterfaceEntry':cOPatchInterfaceEntry,_X:cOPatchIdentifier,_N:cOPatchIndexNext,_O:cOPatchLastChange,_G:cOPatchEventType,'cOPatchTable':cOPatchTable,'cOPatchEntry':cOPatchEntry,_U:cOPatchIndex,_H:cOPatchLowIfIndex,_I:cOPatchHighIfIndex,_J:cOPatchType,_K:cOPatchStatus,_Q:cOPatchCreationTime,_R:cOPatchRowStatus,_Z:cOPatchDirOnLowIf,_P:cOPatchEventEnabled,'cOPatchIntfTable':cOPatchIntfTable,'cOPatchIntfEntry':cOPatchIntfEntry,_W:cOPatchIntfDirection,_Y:cOPatchIntfPatchId,'cOPatchMIBNotifications':cOPatchMIBNotifications,_a:cOPatchEvent,'cOPatchMIBConformance':cOPatchMIBConformance,'cOPatchMIBCompliances':cOPatchMIBCompliances,'cOPatchMIBCompliance':cOPatchMIBCompliance,'cOPatchMIBCompliance1':cOPatchMIBCompliance1,'cOPatchMIBGroups':cOPatchMIBGroups,_b:cOPatchInterfaceGroup,_c:cOPatchGroup,_S:cOPatchNotifyGroup,_d:cOPatchIntfGroup,_e:cOPatchGroup1})