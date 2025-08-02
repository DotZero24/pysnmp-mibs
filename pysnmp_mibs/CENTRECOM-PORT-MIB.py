_F='atiPortLoadshareSlaveIfIndex'
_E='atiPortLoadshareMasterIfIndex'
_D='Integer32'
_C='CENTRECOM-PORT-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extSwitchMIB,=mibBuilder.importSymbols('CENTRECOM-MIB','extSwitchMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
atiPort=ModuleIdentity((1,3,6,1,4,1,207,8,12,2,6))
_AtiPortLoadshareTable_Object=MibTable
atiPortLoadshareTable=_AtiPortLoadshareTable_Object((1,3,6,1,4,1,207,8,12,2,6,1))
if mibBuilder.loadTexts:atiPortLoadshareTable.setStatus(_A)
_AtiPortLoadshareEntry_Object=MibTableRow
atiPortLoadshareEntry=_AtiPortLoadshareEntry_Object((1,3,6,1,4,1,207,8,12,2,6,1,1))
atiPortLoadshareEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:atiPortLoadshareEntry.setStatus(_A)
_AtiPortLoadshareMasterIfIndex_Type=Integer32
_AtiPortLoadshareMasterIfIndex_Object=MibTableColumn
atiPortLoadshareMasterIfIndex=_AtiPortLoadshareMasterIfIndex_Object((1,3,6,1,4,1,207,8,12,2,6,1,1,1),_AtiPortLoadshareMasterIfIndex_Type())
atiPortLoadshareMasterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPortLoadshareMasterIfIndex.setStatus(_A)
_AtiPortLoadshareSlaveIfIndex_Type=Integer32
_AtiPortLoadshareSlaveIfIndex_Object=MibTableColumn
atiPortLoadshareSlaveIfIndex=_AtiPortLoadshareSlaveIfIndex_Object((1,3,6,1,4,1,207,8,12,2,6,1,1,2),_AtiPortLoadshareSlaveIfIndex_Type())
atiPortLoadshareSlaveIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPortLoadshareSlaveIfIndex.setStatus(_A)
class _AtiPortLoadshareGrouping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('pair',2),('quad',4)))
_AtiPortLoadshareGrouping_Type.__name__=_D
_AtiPortLoadshareGrouping_Object=MibTableColumn
atiPortLoadshareGrouping=_AtiPortLoadshareGrouping_Object((1,3,6,1,4,1,207,8,12,2,6,1,1,3),_AtiPortLoadshareGrouping_Type())
atiPortLoadshareGrouping.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPortLoadshareGrouping.setStatus(_A)
_AtiPortLoadshareStatus_Type=RowStatus
_AtiPortLoadshareStatus_Object=MibTableColumn
atiPortLoadshareStatus=_AtiPortLoadshareStatus_Object((1,3,6,1,4,1,207,8,12,2,6,1,1,4),_AtiPortLoadshareStatus_Type())
atiPortLoadshareStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiPortLoadshareStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'atiPort':atiPort,'atiPortLoadshareTable':atiPortLoadshareTable,'atiPortLoadshareEntry':atiPortLoadshareEntry,_E:atiPortLoadshareMasterIfIndex,_F:atiPortLoadshareSlaveIfIndex,'atiPortLoadshareGrouping':atiPortLoadshareGrouping,'atiPortLoadshareStatus':atiPortLoadshareStatus})