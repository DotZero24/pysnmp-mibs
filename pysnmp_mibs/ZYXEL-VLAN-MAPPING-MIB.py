_I='not-accessible'
_H='zyVlanMappingVid'
_G='zyVlanMappingPort'
_F='Integer32'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='ZYXEL-VLAN-MAPPING-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVlanMapping=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,88))
_ZyxelVlanMappingSetup_ObjectIdentity=ObjectIdentity
zyxelVlanMappingSetup=_ZyxelVlanMappingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,88,1))
_ZyVlanMappingState_Type=EnabledStatus
_ZyVlanMappingState_Object=MibScalar
zyVlanMappingState=_ZyVlanMappingState_Object((1,3,6,1,4,1,890,1,15,3,88,1,1),_ZyVlanMappingState_Type())
zyVlanMappingState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanMappingState.setStatus(_A)
_ZyxelVlanMappingPortTable_Object=MibTable
zyxelVlanMappingPortTable=_ZyxelVlanMappingPortTable_Object((1,3,6,1,4,1,890,1,15,3,88,1,2))
if mibBuilder.loadTexts:zyxelVlanMappingPortTable.setStatus(_A)
_ZyxelVlanMappingPortEntry_Object=MibTableRow
zyxelVlanMappingPortEntry=_ZyxelVlanMappingPortEntry_Object((1,3,6,1,4,1,890,1,15,3,88,1,2,1))
zyxelVlanMappingPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelVlanMappingPortEntry.setStatus(_A)
_ZyVlanMappingPortState_Type=EnabledStatus
_ZyVlanMappingPortState_Object=MibTableColumn
zyVlanMappingPortState=_ZyVlanMappingPortState_Object((1,3,6,1,4,1,890,1,15,3,88,1,2,1,1),_ZyVlanMappingPortState_Type())
zyVlanMappingPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanMappingPortState.setStatus(_A)
_ZyVlanMappingMaxNumberOfRules_Type=Integer32
_ZyVlanMappingMaxNumberOfRules_Object=MibScalar
zyVlanMappingMaxNumberOfRules=_ZyVlanMappingMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,88,1,3),_ZyVlanMappingMaxNumberOfRules_Type())
zyVlanMappingMaxNumberOfRules.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyVlanMappingMaxNumberOfRules.setStatus(_A)
_ZyxelVlanMappingTable_Object=MibTable
zyxelVlanMappingTable=_ZyxelVlanMappingTable_Object((1,3,6,1,4,1,890,1,15,3,88,1,4))
if mibBuilder.loadTexts:zyxelVlanMappingTable.setStatus(_A)
_ZyxelVlanMappingEntry_Object=MibTableRow
zyxelVlanMappingEntry=_ZyxelVlanMappingEntry_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1))
zyxelVlanMappingEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:zyxelVlanMappingEntry.setStatus(_A)
_ZyVlanMappingName_Type=DisplayString
_ZyVlanMappingName_Object=MibTableColumn
zyVlanMappingName=_ZyVlanMappingName_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,1),_ZyVlanMappingName_Type())
zyVlanMappingName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanMappingName.setStatus(_A)
_ZyVlanMappingPort_Type=Integer32
_ZyVlanMappingPort_Object=MibTableColumn
zyVlanMappingPort=_ZyVlanMappingPort_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,2),_ZyVlanMappingPort_Type())
zyVlanMappingPort.setMaxAccess(_I)
if mibBuilder.loadTexts:zyVlanMappingPort.setStatus(_A)
_ZyVlanMappingVid_Type=Integer32
_ZyVlanMappingVid_Object=MibTableColumn
zyVlanMappingVid=_ZyVlanMappingVid_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,3),_ZyVlanMappingVid_Type())
zyVlanMappingVid.setMaxAccess(_I)
if mibBuilder.loadTexts:zyVlanMappingVid.setStatus(_A)
_ZyVlanMappingTranslatedVid_Type=Integer32
_ZyVlanMappingTranslatedVid_Object=MibTableColumn
zyVlanMappingTranslatedVid=_ZyVlanMappingTranslatedVid_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,4),_ZyVlanMappingTranslatedVid_Type())
zyVlanMappingTranslatedVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanMappingTranslatedVid.setStatus(_A)
class _ZyVlanMappingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('priority0',0),('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7)))
_ZyVlanMappingPriority_Type.__name__=_F
_ZyVlanMappingPriority_Object=MibTableColumn
zyVlanMappingPriority=_ZyVlanMappingPriority_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,5),_ZyVlanMappingPriority_Type())
zyVlanMappingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanMappingPriority.setStatus(_A)
_ZyVlanMappingRowStatus_Type=RowStatus
_ZyVlanMappingRowStatus_Object=MibTableColumn
zyVlanMappingRowStatus=_ZyVlanMappingRowStatus_Object((1,3,6,1,4,1,890,1,15,3,88,1,4,1,6),_ZyVlanMappingRowStatus_Type())
zyVlanMappingRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyVlanMappingRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelVlanMapping':zyxelVlanMapping,'zyxelVlanMappingSetup':zyxelVlanMappingSetup,'zyVlanMappingState':zyVlanMappingState,'zyxelVlanMappingPortTable':zyxelVlanMappingPortTable,'zyxelVlanMappingPortEntry':zyxelVlanMappingPortEntry,'zyVlanMappingPortState':zyVlanMappingPortState,'zyVlanMappingMaxNumberOfRules':zyVlanMappingMaxNumberOfRules,'zyxelVlanMappingTable':zyxelVlanMappingTable,'zyxelVlanMappingEntry':zyxelVlanMappingEntry,'zyVlanMappingName':zyVlanMappingName,_G:zyVlanMappingPort,_H:zyVlanMappingVid,'zyVlanMappingTranslatedVid':zyVlanMappingTranslatedVid,'zyVlanMappingPriority':zyVlanMappingPriority,'zyVlanMappingRowStatus':zyVlanMappingRowStatus})