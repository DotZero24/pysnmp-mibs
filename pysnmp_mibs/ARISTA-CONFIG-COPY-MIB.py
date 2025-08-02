_S='aristaConfigCopyObjectsGroup'
_R='aristaConfigCopyRowStatus'
_Q='aristaConfigCopyFailureMessage'
_P='aristaConfigCopyFailureCause'
_O='aristaConfigCopyTimeCompleted'
_N='aristaConfigCopyTimeStarted'
_M='aristaConfigCopyTimeout'
_L='aristaConfigCopyState'
_K='aristaConfigCopyDestUri'
_J='aristaConfigCopySourceUri'
_I='not-accessible'
_H='aristaConfigCopyId'
_G='aristaConfigCopyName'
_F='Unsigned32'
_E='OctetString'
_D='read-create'
_C='read-only'
_B='ARISTA-CONFIG-COPY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
aristaConfigCopyMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,7))
if mibBuilder.loadTexts:aristaConfigCopyMIB.setRevisions(('2021-09-08 00:00','2014-08-15 00:00','2013-02-14 00:00'))
class ConfigCopyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('inactive',0),('scheduled',1),('running',2),('completed',3),('failed',4)))
class ConfigCopyFailureCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('unknown',1),('timeout',2)))
_AristaConfigCopyCommandTable_Object=MibTable
aristaConfigCopyCommandTable=_AristaConfigCopyCommandTable_Object((1,3,6,1,4,1,30065,3,7,1))
if mibBuilder.loadTexts:aristaConfigCopyCommandTable.setStatus(_A)
_AristaConfigCopyCommandEntry_Object=MibTableRow
aristaConfigCopyCommandEntry=_AristaConfigCopyCommandEntry_Object((1,3,6,1,4,1,30065,3,7,1,1))
aristaConfigCopyCommandEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:aristaConfigCopyCommandEntry.setStatus(_A)
class _AristaConfigCopyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,114))
_AristaConfigCopyName_Type.__name__=_E
_AristaConfigCopyName_Object=MibTableColumn
aristaConfigCopyName=_AristaConfigCopyName_Object((1,3,6,1,4,1,30065,3,7,1,1,1),_AristaConfigCopyName_Type())
aristaConfigCopyName.setMaxAccess(_I)
if mibBuilder.loadTexts:aristaConfigCopyName.setStatus(_A)
_AristaConfigCopyId_Type=Unsigned32
_AristaConfigCopyId_Object=MibTableColumn
aristaConfigCopyId=_AristaConfigCopyId_Object((1,3,6,1,4,1,30065,3,7,1,1,2),_AristaConfigCopyId_Type())
aristaConfigCopyId.setMaxAccess(_I)
if mibBuilder.loadTexts:aristaConfigCopyId.setStatus(_A)
_AristaConfigCopySourceUri_Type=OctetString
_AristaConfigCopySourceUri_Object=MibTableColumn
aristaConfigCopySourceUri=_AristaConfigCopySourceUri_Object((1,3,6,1,4,1,30065,3,7,1,1,3),_AristaConfigCopySourceUri_Type())
aristaConfigCopySourceUri.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaConfigCopySourceUri.setStatus(_A)
_AristaConfigCopyDestUri_Type=OctetString
_AristaConfigCopyDestUri_Object=MibTableColumn
aristaConfigCopyDestUri=_AristaConfigCopyDestUri_Object((1,3,6,1,4,1,30065,3,7,1,1,4),_AristaConfigCopyDestUri_Type())
aristaConfigCopyDestUri.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaConfigCopyDestUri.setStatus(_A)
_AristaConfigCopyState_Type=ConfigCopyState
_AristaConfigCopyState_Object=MibTableColumn
aristaConfigCopyState=_AristaConfigCopyState_Object((1,3,6,1,4,1,30065,3,7,1,1,5),_AristaConfigCopyState_Type())
aristaConfigCopyState.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaConfigCopyState.setStatus(_A)
class _AristaConfigCopyTimeout_Type(Unsigned32):defaultValue=60
_AristaConfigCopyTimeout_Type.__name__=_F
_AristaConfigCopyTimeout_Object=MibTableColumn
aristaConfigCopyTimeout=_AristaConfigCopyTimeout_Object((1,3,6,1,4,1,30065,3,7,1,1,6),_AristaConfigCopyTimeout_Type())
aristaConfigCopyTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaConfigCopyTimeout.setStatus(_A)
_AristaConfigCopyTimeStarted_Type=DateAndTime
_AristaConfigCopyTimeStarted_Object=MibTableColumn
aristaConfigCopyTimeStarted=_AristaConfigCopyTimeStarted_Object((1,3,6,1,4,1,30065,3,7,1,1,7),_AristaConfigCopyTimeStarted_Type())
aristaConfigCopyTimeStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaConfigCopyTimeStarted.setStatus(_A)
_AristaConfigCopyTimeCompleted_Type=DateAndTime
_AristaConfigCopyTimeCompleted_Object=MibTableColumn
aristaConfigCopyTimeCompleted=_AristaConfigCopyTimeCompleted_Object((1,3,6,1,4,1,30065,3,7,1,1,8),_AristaConfigCopyTimeCompleted_Type())
aristaConfigCopyTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaConfigCopyTimeCompleted.setStatus(_A)
_AristaConfigCopyFailureCause_Type=ConfigCopyFailureCause
_AristaConfigCopyFailureCause_Object=MibTableColumn
aristaConfigCopyFailureCause=_AristaConfigCopyFailureCause_Object((1,3,6,1,4,1,30065,3,7,1,1,9),_AristaConfigCopyFailureCause_Type())
aristaConfigCopyFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaConfigCopyFailureCause.setStatus(_A)
_AristaConfigCopyFailureMessage_Type=OctetString
_AristaConfigCopyFailureMessage_Object=MibTableColumn
aristaConfigCopyFailureMessage=_AristaConfigCopyFailureMessage_Object((1,3,6,1,4,1,30065,3,7,1,1,10),_AristaConfigCopyFailureMessage_Type())
aristaConfigCopyFailureMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaConfigCopyFailureMessage.setStatus(_A)
_AristaConfigCopyRowStatus_Type=RowStatus
_AristaConfigCopyRowStatus_Object=MibTableColumn
aristaConfigCopyRowStatus=_AristaConfigCopyRowStatus_Object((1,3,6,1,4,1,30065,3,7,1,1,11),_AristaConfigCopyRowStatus_Type())
aristaConfigCopyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaConfigCopyRowStatus.setStatus(_A)
_AristaConfigCopyConformance_ObjectIdentity=ObjectIdentity
aristaConfigCopyConformance=_AristaConfigCopyConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,7,2))
_AristaConfigCopyCompliances_ObjectIdentity=ObjectIdentity
aristaConfigCopyCompliances=_AristaConfigCopyCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,7,2,1))
_AristaConfigCopyGroups_ObjectIdentity=ObjectIdentity
aristaConfigCopyGroups=_AristaConfigCopyGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,7,2,2))
aristaConfigCopyObjectsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,7,2,2,1))
aristaConfigCopyObjectsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:aristaConfigCopyObjectsGroup.setStatus(_A)
aristaConfigCopyCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,7,2,1,1))
aristaConfigCopyCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:aristaConfigCopyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigCopyState':ConfigCopyState,'ConfigCopyFailureCause':ConfigCopyFailureCause,'aristaConfigCopyMIB':aristaConfigCopyMIB,'aristaConfigCopyCommandTable':aristaConfigCopyCommandTable,'aristaConfigCopyCommandEntry':aristaConfigCopyCommandEntry,_G:aristaConfigCopyName,_H:aristaConfigCopyId,_J:aristaConfigCopySourceUri,_K:aristaConfigCopyDestUri,_L:aristaConfigCopyState,_M:aristaConfigCopyTimeout,_N:aristaConfigCopyTimeStarted,_O:aristaConfigCopyTimeCompleted,_P:aristaConfigCopyFailureCause,_Q:aristaConfigCopyFailureMessage,_R:aristaConfigCopyRowStatus,'aristaConfigCopyConformance':aristaConfigCopyConformance,'aristaConfigCopyCompliances':aristaConfigCopyCompliances,'aristaConfigCopyCompliance':aristaConfigCopyCompliance,'aristaConfigCopyGroups':aristaConfigCopyGroups,_S:aristaConfigCopyObjectsGroup})