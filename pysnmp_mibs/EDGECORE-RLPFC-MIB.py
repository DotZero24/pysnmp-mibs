_H='rlPfcPriority'
_G='EDGECORE-RLPFC-MIB'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlPfcMib=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,148))
if mibBuilder.loadTexts:rlPfcMib.setRevisions(('2010-04-18 00:00',))
class RlPfcPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlPfcGlobalEnable_Type=TruthValue
_RlPfcGlobalEnable_Object=MibScalar
rlPfcGlobalEnable=_RlPfcGlobalEnable_Object((1,3,6,1,4,1,259,10,1,14,89,148,1),_RlPfcGlobalEnable_Type())
rlPfcGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPfcGlobalEnable.setStatus(_A)
_RlPfcPortTable_Object=MibTable
rlPfcPortTable=_RlPfcPortTable_Object((1,3,6,1,4,1,259,10,1,14,89,148,2))
if mibBuilder.loadTexts:rlPfcPortTable.setStatus(_A)
_RlPfcPortEntry_Object=MibTableRow
rlPfcPortEntry=_RlPfcPortEntry_Object((1,3,6,1,4,1,259,10,1,14,89,148,2,1))
rlPfcPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPfcPortEntry.setStatus(_A)
_RlPfcPortEnableAdmin_Type=TruthValue
_RlPfcPortEnableAdmin_Object=MibTableColumn
rlPfcPortEnableAdmin=_RlPfcPortEnableAdmin_Object((1,3,6,1,4,1,259,10,1,14,89,148,2,1,1),_RlPfcPortEnableAdmin_Type())
rlPfcPortEnableAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPfcPortEnableAdmin.setStatus(_A)
_RlPfcPortEnableOper_Type=TruthValue
_RlPfcPortEnableOper_Object=MibTableColumn
rlPfcPortEnableOper=_RlPfcPortEnableOper_Object((1,3,6,1,4,1,259,10,1,14,89,148,2,1,2),_RlPfcPortEnableOper_Type())
rlPfcPortEnableOper.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPfcPortEnableOper.setStatus(_A)
_RlPfcPriorityTable_Object=MibTable
rlPfcPriorityTable=_RlPfcPriorityTable_Object((1,3,6,1,4,1,259,10,1,14,89,148,3))
if mibBuilder.loadTexts:rlPfcPriorityTable.setStatus(_A)
_RlPfcPriorityEntry_Object=MibTableRow
rlPfcPriorityEntry=_RlPfcPriorityEntry_Object((1,3,6,1,4,1,259,10,1,14,89,148,3,1))
rlPfcPriorityEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rlPfcPriorityEntry.setStatus(_A)
_RlPfcPriority_Type=RlPfcPriority
_RlPfcPriority_Object=MibTableColumn
rlPfcPriority=_RlPfcPriority_Object((1,3,6,1,4,1,259,10,1,14,89,148,3,1,1),_RlPfcPriority_Type())
rlPfcPriority.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlPfcPriority.setStatus(_A)
_RlPfcPriorityEnable_Type=TruthValue
_RlPfcPriorityEnable_Object=MibTableColumn
rlPfcPriorityEnable=_RlPfcPriorityEnable_Object((1,3,6,1,4,1,259,10,1,14,89,148,3,1,2),_RlPfcPriorityEnable_Type())
rlPfcPriorityEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPfcPriorityEnable.setStatus(_A)
_RlPfcPriorityEnableOperStatus_Type=TruthValue
_RlPfcPriorityEnableOperStatus_Object=MibTableColumn
rlPfcPriorityEnableOperStatus=_RlPfcPriorityEnableOperStatus_Object((1,3,6,1,4,1,259,10,1,14,89,148,3,1,3),_RlPfcPriorityEnableOperStatus_Type())
rlPfcPriorityEnableOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPfcPriorityEnableOperStatus.setStatus(_A)
class _RlPfcPriorityEnableOperStatusReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('pfcGlobalDis',2),('pfcPriorityAdminDis',3),('queue0',4),('sharedQueue',5),('notSameQueue',6)))
_RlPfcPriorityEnableOperStatusReason_Type.__name__=_F
_RlPfcPriorityEnableOperStatusReason_Object=MibTableColumn
rlPfcPriorityEnableOperStatusReason=_RlPfcPriorityEnableOperStatusReason_Object((1,3,6,1,4,1,259,10,1,14,89,148,3,1,4),_RlPfcPriorityEnableOperStatusReason_Type())
rlPfcPriorityEnableOperStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPfcPriorityEnableOperStatusReason.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'RlPfcPriority':RlPfcPriority,'rlPfcMib':rlPfcMib,'rlPfcGlobalEnable':rlPfcGlobalEnable,'rlPfcPortTable':rlPfcPortTable,'rlPfcPortEntry':rlPfcPortEntry,'rlPfcPortEnableAdmin':rlPfcPortEnableAdmin,'rlPfcPortEnableOper':rlPfcPortEnableOper,'rlPfcPriorityTable':rlPfcPriorityTable,'rlPfcPriorityEntry':rlPfcPriorityEntry,_H:rlPfcPriority,'rlPfcPriorityEnable':rlPfcPriorityEnable,'rlPfcPriorityEnableOperStatus':rlPfcPriorityEnableOperStatus,'rlPfcPriorityEnableOperStatusReason':rlPfcPriorityEnableOperStatusReason})