_J='aristaGeneralMibGroup'
_I='aristaReloadTime'
_H='aristaReloadCauseDescription'
_G='read-only'
_F='aristaReloadCauseIndex'
_E='aristaReloadIndex'
_D='aristaReloadUnitIndex'
_C='not-accessible'
_B='ARISTA-GENERAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
aristaGeneralMib=ModuleIdentity((1,3,6,1,4,1,30065,3,24))
if mibBuilder.loadTexts:aristaGeneralMib.setRevisions(('2017-11-06 00:00',))
_AristaGeneralMibNotifications_ObjectIdentity=ObjectIdentity
aristaGeneralMibNotifications=_AristaGeneralMibNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,24,0))
_AristaGeneralMibObjects_ObjectIdentity=ObjectIdentity
aristaGeneralMibObjects=_AristaGeneralMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,24,1))
_AristaReloadCauseTable_Object=MibTable
aristaReloadCauseTable=_AristaReloadCauseTable_Object((1,3,6,1,4,1,30065,3,24,1,1))
if mibBuilder.loadTexts:aristaReloadCauseTable.setStatus(_A)
_AristaReloadCauseEntry_Object=MibTableRow
aristaReloadCauseEntry=_AristaReloadCauseEntry_Object((1,3,6,1,4,1,30065,3,24,1,1,1))
aristaReloadCauseEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:aristaReloadCauseEntry.setStatus(_A)
_AristaReloadUnitIndex_Type=Unsigned32
_AristaReloadUnitIndex_Object=MibTableColumn
aristaReloadUnitIndex=_AristaReloadUnitIndex_Object((1,3,6,1,4,1,30065,3,24,1,1,1,1),_AristaReloadUnitIndex_Type())
aristaReloadUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaReloadUnitIndex.setStatus(_A)
_AristaReloadIndex_Type=Unsigned32
_AristaReloadIndex_Object=MibTableColumn
aristaReloadIndex=_AristaReloadIndex_Object((1,3,6,1,4,1,30065,3,24,1,1,1,2),_AristaReloadIndex_Type())
aristaReloadIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaReloadIndex.setStatus(_A)
_AristaReloadCauseIndex_Type=Unsigned32
_AristaReloadCauseIndex_Object=MibTableColumn
aristaReloadCauseIndex=_AristaReloadCauseIndex_Object((1,3,6,1,4,1,30065,3,24,1,1,1,3),_AristaReloadCauseIndex_Type())
aristaReloadCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaReloadCauseIndex.setStatus(_A)
_AristaReloadCauseDescription_Type=OctetString
_AristaReloadCauseDescription_Object=MibTableColumn
aristaReloadCauseDescription=_AristaReloadCauseDescription_Object((1,3,6,1,4,1,30065,3,24,1,1,1,4),_AristaReloadCauseDescription_Type())
aristaReloadCauseDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaReloadCauseDescription.setStatus(_A)
_AristaReloadTime_Type=DateAndTime
_AristaReloadTime_Object=MibTableColumn
aristaReloadTime=_AristaReloadTime_Object((1,3,6,1,4,1,30065,3,24,1,1,1,5),_AristaReloadTime_Type())
aristaReloadTime.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaReloadTime.setStatus(_A)
_AristaGeneralMibConformance_ObjectIdentity=ObjectIdentity
aristaGeneralMibConformance=_AristaGeneralMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,24,2))
_AristaGeneralMibCompliances_ObjectIdentity=ObjectIdentity
aristaGeneralMibCompliances=_AristaGeneralMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,24,2,1))
_AristaGeneralMibGroups_ObjectIdentity=ObjectIdentity
aristaGeneralMibGroups=_AristaGeneralMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,24,2,2))
aristaGeneralMibGroup=ObjectGroup((1,3,6,1,4,1,30065,3,24,2,2,1))
aristaGeneralMibGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:aristaGeneralMibGroup.setStatus(_A)
aristaGeneralMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,24,2,1,1))
aristaGeneralMibCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:aristaGeneralMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaGeneralMib':aristaGeneralMib,'aristaGeneralMibNotifications':aristaGeneralMibNotifications,'aristaGeneralMibObjects':aristaGeneralMibObjects,'aristaReloadCauseTable':aristaReloadCauseTable,'aristaReloadCauseEntry':aristaReloadCauseEntry,_D:aristaReloadUnitIndex,_E:aristaReloadIndex,_F:aristaReloadCauseIndex,_H:aristaReloadCauseDescription,_I:aristaReloadTime,'aristaGeneralMibConformance':aristaGeneralMibConformance,'aristaGeneralMibCompliances':aristaGeneralMibCompliances,'aristaGeneralMibCompliance':aristaGeneralMibCompliance,'aristaGeneralMibGroups':aristaGeneralMibGroups,_J:aristaGeneralMibGroup})