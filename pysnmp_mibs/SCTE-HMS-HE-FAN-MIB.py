_K='heFanStatusGroup'
_J='heFanUnitMandatoryGroup'
_I='heFanStatusCurrent'
_H='heFanStatusAlarm'
_G='heFanUnitAlarm'
_F='heFanStatusIndex'
_E='read-only'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='SCTE-HMS-HE-FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
HeFaultStatus,HeMilliAmp,heFans=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeFaultStatus','HeMilliAmp','heFans')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heFanModuleMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,2,3,1))
_HeFanMIBObjects_ObjectIdentity=ObjectIdentity
heFanMIBObjects=_HeFanMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,3,1,1))
_HeFanUnitTable_Object=MibTable
heFanUnitTable=_HeFanUnitTable_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,1))
if mibBuilder.loadTexts:heFanUnitTable.setStatus(_A)
_HeFanUnitEntry_Object=MibTableRow
heFanUnitEntry=_HeFanUnitEntry_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,1,1))
heFanUnitEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:heFanUnitEntry.setStatus(_A)
_HeFanUnitAlarm_Type=HeFaultStatus
_HeFanUnitAlarm_Object=MibTableColumn
heFanUnitAlarm=_HeFanUnitAlarm_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,1,1,1),_HeFanUnitAlarm_Type())
heFanUnitAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:heFanUnitAlarm.setStatus(_A)
_HeFanStatusTable_Object=MibTable
heFanStatusTable=_HeFanStatusTable_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,2))
if mibBuilder.loadTexts:heFanStatusTable.setStatus(_A)
_HeFanStatusEntry_Object=MibTableRow
heFanStatusEntry=_HeFanStatusEntry_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,2,1))
heFanStatusEntry.setIndexNames((0,_C,_D),(0,_B,_F))
if mibBuilder.loadTexts:heFanStatusEntry.setStatus(_A)
_HeFanStatusIndex_Type=Unsigned32
_HeFanStatusIndex_Object=MibTableColumn
heFanStatusIndex=_HeFanStatusIndex_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,2,1,1),_HeFanStatusIndex_Type())
heFanStatusIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:heFanStatusIndex.setStatus(_A)
_HeFanStatusCurrent_Type=HeMilliAmp
_HeFanStatusCurrent_Object=MibTableColumn
heFanStatusCurrent=_HeFanStatusCurrent_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,2,1,2),_HeFanStatusCurrent_Type())
heFanStatusCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:heFanStatusCurrent.setStatus(_A)
if mibBuilder.loadTexts:heFanStatusCurrent.setUnits('milliamperes')
_HeFanStatusAlarm_Type=HeFaultStatus
_HeFanStatusAlarm_Object=MibTableColumn
heFanStatusAlarm=_HeFanStatusAlarm_Object((1,3,6,1,4,1,5591,1,11,2,3,1,1,2,1,3),_HeFanStatusAlarm_Type())
heFanStatusAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:heFanStatusAlarm.setStatus(_A)
_HeFanMIBConformance_ObjectIdentity=ObjectIdentity
heFanMIBConformance=_HeFanMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,3,1,2))
_HeFanMIBCompliances_ObjectIdentity=ObjectIdentity
heFanMIBCompliances=_HeFanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,3,1,2,1))
_HeFanMIBGroups_ObjectIdentity=ObjectIdentity
heFanMIBGroups=_HeFanMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,3,1,2,2))
heFanUnitMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,3,1,2,2,1))
heFanUnitMandatoryGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:heFanUnitMandatoryGroup.setStatus(_A)
heFanStatusGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,3,1,2,2,2))
heFanStatusGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:heFanStatusGroup.setStatus(_A)
heFanCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,2,3,1,2,1,1))
heFanCompliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:heFanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heFanModuleMIB':heFanModuleMIB,'heFanMIBObjects':heFanMIBObjects,'heFanUnitTable':heFanUnitTable,'heFanUnitEntry':heFanUnitEntry,_G:heFanUnitAlarm,'heFanStatusTable':heFanStatusTable,'heFanStatusEntry':heFanStatusEntry,_F:heFanStatusIndex,_I:heFanStatusCurrent,_H:heFanStatusAlarm,'heFanMIBConformance':heFanMIBConformance,'heFanMIBCompliances':heFanMIBCompliances,'heFanCompliance':heFanCompliance,'heFanMIBGroups':heFanMIBGroups,_J:heFanUnitMandatoryGroup,_K:heFanStatusGroup})