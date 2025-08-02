_G='nbPortMediaSelectGroup'
_F='nbPortMediaSelectStatus'
_E='nbPortMediaSelectMode'
_D='nbPortMediaSelectPort'
_C='Integer32'
_B='OA-PORTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbPortMediaSelectMIB=ModuleIdentity((1,3,6,1,4,1,629,1,50,10,10))
if mibBuilder.loadTexts:nbPortMediaSelectMIB.setRevisions(('2006-03-08 00:00',))
_NbPortParams_ObjectIdentity=ObjectIdentity
nbPortParams=_NbPortParams_ObjectIdentity((1,3,6,1,4,1,629,1,50,10))
_NbPortMediaSelectTable_Object=MibTable
nbPortMediaSelectTable=_NbPortMediaSelectTable_Object((1,3,6,1,4,1,629,1,50,10,10,5))
if mibBuilder.loadTexts:nbPortMediaSelectTable.setStatus(_A)
_NbPortMediaSelectEntry_Object=MibTableRow
nbPortMediaSelectEntry=_NbPortMediaSelectEntry_Object((1,3,6,1,4,1,629,1,50,10,10,5,1))
nbPortMediaSelectEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:nbPortMediaSelectEntry.setStatus(_A)
class _NbPortMediaSelectPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbPortMediaSelectPort_Type.__name__=_C
_NbPortMediaSelectPort_Object=MibTableColumn
nbPortMediaSelectPort=_NbPortMediaSelectPort_Object((1,3,6,1,4,1,629,1,50,10,10,5,1,1),_NbPortMediaSelectPort_Type())
nbPortMediaSelectPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbPortMediaSelectPort.setStatus(_A)
class _NbPortMediaSelectMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('autoSelect',2),('forceRJ45',3),('forceSFP',4),('forceSFP100',5)))
_NbPortMediaSelectMode_Type.__name__=_C
_NbPortMediaSelectMode_Object=MibTableColumn
nbPortMediaSelectMode=_NbPortMediaSelectMode_Object((1,3,6,1,4,1,629,1,50,10,10,5,1,2),_NbPortMediaSelectMode_Type())
nbPortMediaSelectMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbPortMediaSelectMode.setStatus(_A)
class _NbPortMediaSelectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('rj45',2),('sfp',3),('sfp100',4)))
_NbPortMediaSelectStatus_Type.__name__=_C
_NbPortMediaSelectStatus_Object=MibTableColumn
nbPortMediaSelectStatus=_NbPortMediaSelectStatus_Object((1,3,6,1,4,1,629,1,50,10,10,5,1,3),_NbPortMediaSelectStatus_Type())
nbPortMediaSelectStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:nbPortMediaSelectStatus.setStatus(_A)
_NbPortMediaSelectConformance_ObjectIdentity=ObjectIdentity
nbPortMediaSelectConformance=_NbPortMediaSelectConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,10,101))
_NbPortMediaSelectMIBCompliances_ObjectIdentity=ObjectIdentity
nbPortMediaSelectMIBCompliances=_NbPortMediaSelectMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,10,101,1))
_NbPortMediaSelectMIBGroups_ObjectIdentity=ObjectIdentity
nbPortMediaSelectMIBGroups=_NbPortMediaSelectMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,10,101,2))
nbPortMediaSelectGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,10,10,101,2,2))
nbPortMediaSelectGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:nbPortMediaSelectGroup.setStatus(_A)
nbPortMediaSelectMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,10,10,101,1,1))
nbPortMediaSelectMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:nbPortMediaSelectMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbPortParams':nbPortParams,'nbPortMediaSelectMIB':nbPortMediaSelectMIB,'nbPortMediaSelectTable':nbPortMediaSelectTable,'nbPortMediaSelectEntry':nbPortMediaSelectEntry,_D:nbPortMediaSelectPort,_E:nbPortMediaSelectMode,_F:nbPortMediaSelectStatus,'nbPortMediaSelectConformance':nbPortMediaSelectConformance,'nbPortMediaSelectMIBCompliances':nbPortMediaSelectMIBCompliances,'nbPortMediaSelectMIBCompliance':nbPortMediaSelectMIBCompliance,'nbPortMediaSelectMIBGroups':nbPortMediaSelectMIBGroups,_G:nbPortMediaSelectGroup})