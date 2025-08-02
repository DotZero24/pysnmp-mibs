_M='fseGroup'
_L='fsePathLossInvokedPortAid'
_K='fseIsPathLossCheckInvoked'
_J='fseOlosSoakTime'
_I='fseProvEqptType'
_H='fseMoId'
_G='read-only'
_F='Integer32'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-FSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fseMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,38))
_FseTable_Object=MibTable
fseTable=_FseTable_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1))
if mibBuilder.loadTexts:fseTable.setStatus(_A)
_FseEntry_Object=MibTableRow
fseEntry=_FseEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1))
fseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fseEntry.setStatus(_A)
_FseMoId_Type=DisplayString
_FseMoId_Object=MibTableColumn
fseMoId=_FseMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1,1),_FseMoId_Type())
fseMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:fseMoId.setStatus(_A)
_FseProvEqptType_Type=InfnEqptType
_FseProvEqptType_Object=MibTableColumn
fseProvEqptType=_FseProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1,2),_FseProvEqptType_Type())
fseProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:fseProvEqptType.setStatus(_A)
class _FseOlosSoakTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fast',1),('medium',2),('long',3)))
_FseOlosSoakTime_Type.__name__=_F
_FseOlosSoakTime_Object=MibTableColumn
fseOlosSoakTime=_FseOlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1,3),_FseOlosSoakTime_Type())
fseOlosSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fseOlosSoakTime.setStatus(_A)
_FseIsPathLossCheckInvoked_Type=TruthValue
_FseIsPathLossCheckInvoked_Object=MibTableColumn
fseIsPathLossCheckInvoked=_FseIsPathLossCheckInvoked_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1,4),_FseIsPathLossCheckInvoked_Type())
fseIsPathLossCheckInvoked.setMaxAccess(_G)
if mibBuilder.loadTexts:fseIsPathLossCheckInvoked.setStatus(_A)
_FsePathLossInvokedPortAid_Type=DisplayString
_FsePathLossInvokedPortAid_Object=MibTableColumn
fsePathLossInvokedPortAid=_FsePathLossInvokedPortAid_Object((1,3,6,1,4,1,21296,2,2,2,1,38,1,1,5),_FsePathLossInvokedPortAid_Type())
fsePathLossInvokedPortAid.setMaxAccess(_G)
if mibBuilder.loadTexts:fsePathLossInvokedPortAid.setStatus(_A)
_FseConffseance_ObjectIdentity=ObjectIdentity
fseConffseance=_FseConffseance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,38,3))
_FseCompliances_ObjectIdentity=ObjectIdentity
fseCompliances=_FseCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,38,3,1))
_FseGroups_ObjectIdentity=ObjectIdentity
fseGroups=_FseGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,38,3,2))
fseGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,38,3,2,1))
fseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fseGroup.setStatus(_A)
fseCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,38,3,1,1))
fseCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:fseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fseMIB':fseMIB,'fseTable':fseTable,'fseEntry':fseEntry,_H:fseMoId,_I:fseProvEqptType,_J:fseOlosSoakTime,_K:fseIsPathLossCheckInvoked,_L:fsePathLossInvokedPortAid,'fseConffseance':fseConffseance,'fseCompliances':fseCompliances,'fseCompliance':fseCompliance,'fseGroups':fseGroups,_M:fseGroup})