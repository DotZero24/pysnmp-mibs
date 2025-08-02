_L='hpicfSlotStatsModuleCpuStatUpdateFrequency'
_K='hpicfSlotStatsModuleCpuStatAveragePercent'
_J='hpicfSlotStatsModuleCpuStatCurrentPercent'
_I='hpicfSlotStatsModuleSerialNum'
_H='hpicfSlotStatsModuleHwModel'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='hpicfSlotStatsGroup'
_D='Integer32'
_C='read-only'
_B='HP-ICF-SLOT-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
hpSwitchStatistics,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitchStatistics')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfSlotStatsMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,20))
if mibBuilder.loadTexts:hpicfSlotStatsMIB.setRevisions(('2012-01-05 00:00',))
_HpicfSlotStatsObjects_ObjectIdentity=ObjectIdentity
hpicfSlotStatsObjects=_HpicfSlotStatsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1))
_HpicfSlotStatsModuleCpuStatTable_Object=MibTable
hpicfSlotStatsModuleCpuStatTable=_HpicfSlotStatsModuleCpuStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1))
if mibBuilder.loadTexts:hpicfSlotStatsModuleCpuStatTable.setStatus(_A)
_HpicfSlotStatsModuleCpuStatEntry_Object=MibTableRow
hpicfSlotStatsModuleCpuStatEntry=_HpicfSlotStatsModuleCpuStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1,1))
hpicfSlotStatsModuleCpuStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfSlotStatsModuleCpuStatEntry.setStatus(_A)
_HpicfSlotStatsModuleHwModel_Type=SnmpAdminString
_HpicfSlotStatsModuleHwModel_Object=MibTableColumn
hpicfSlotStatsModuleHwModel=_HpicfSlotStatsModuleHwModel_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1,1,1),_HpicfSlotStatsModuleHwModel_Type())
hpicfSlotStatsModuleHwModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSlotStatsModuleHwModel.setStatus(_A)
_HpicfSlotStatsModuleSerialNum_Type=SnmpAdminString
_HpicfSlotStatsModuleSerialNum_Object=MibTableColumn
hpicfSlotStatsModuleSerialNum=_HpicfSlotStatsModuleSerialNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1,1,2),_HpicfSlotStatsModuleSerialNum_Type())
hpicfSlotStatsModuleSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSlotStatsModuleSerialNum.setStatus(_A)
class _HpicfSlotStatsModuleCpuStatCurrentPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpicfSlotStatsModuleCpuStatCurrentPercent_Type.__name__=_D
_HpicfSlotStatsModuleCpuStatCurrentPercent_Object=MibTableColumn
hpicfSlotStatsModuleCpuStatCurrentPercent=_HpicfSlotStatsModuleCpuStatCurrentPercent_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1,1,3),_HpicfSlotStatsModuleCpuStatCurrentPercent_Type())
hpicfSlotStatsModuleCpuStatCurrentPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSlotStatsModuleCpuStatCurrentPercent.setStatus(_A)
class _HpicfSlotStatsModuleCpuStatAveragePercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpicfSlotStatsModuleCpuStatAveragePercent_Type.__name__=_D
_HpicfSlotStatsModuleCpuStatAveragePercent_Object=MibTableColumn
hpicfSlotStatsModuleCpuStatAveragePercent=_HpicfSlotStatsModuleCpuStatAveragePercent_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,1,1,4),_HpicfSlotStatsModuleCpuStatAveragePercent_Type())
hpicfSlotStatsModuleCpuStatAveragePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSlotStatsModuleCpuStatAveragePercent.setStatus(_A)
_HpicfSlotStatsModuleCpuStatUpdateFrequency_Type=Integer32
_HpicfSlotStatsModuleCpuStatUpdateFrequency_Object=MibScalar
hpicfSlotStatsModuleCpuStatUpdateFrequency=_HpicfSlotStatsModuleCpuStatUpdateFrequency_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,20,1,2),_HpicfSlotStatsModuleCpuStatUpdateFrequency_Type())
hpicfSlotStatsModuleCpuStatUpdateFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSlotStatsModuleCpuStatUpdateFrequency.setStatus(_A)
_HpicfSlotStatsConformance_ObjectIdentity=ObjectIdentity
hpicfSlotStatsConformance=_HpicfSlotStatsConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2))
_HpicfSlotStatsGroups_ObjectIdentity=ObjectIdentity
hpicfSlotStatsGroups=_HpicfSlotStatsGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2,1))
_HpicfSlotStatsCompliances_ObjectIdentity=ObjectIdentity
hpicfSlotStatsCompliances=_HpicfSlotStatsCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2,2))
hpicfSlotStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2,1,1))
hpicfSlotStatsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfSlotStatsGroup.setStatus(_A)
hpicfSlotStatsFullCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2,2,1))
hpicfSlotStatsFullCompliance1.setObjects((_B,_E))
if mibBuilder.loadTexts:hpicfSlotStatsFullCompliance1.setStatus(_A)
hpicfModuleSlotStatsReadOnlyCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,9,20,2,2,2))
hpicfModuleSlotStatsReadOnlyCompliance1.setObjects((_B,_E))
if mibBuilder.loadTexts:hpicfModuleSlotStatsReadOnlyCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfSlotStatsMIB':hpicfSlotStatsMIB,'hpicfSlotStatsObjects':hpicfSlotStatsObjects,'hpicfSlotStatsModuleCpuStatTable':hpicfSlotStatsModuleCpuStatTable,'hpicfSlotStatsModuleCpuStatEntry':hpicfSlotStatsModuleCpuStatEntry,_H:hpicfSlotStatsModuleHwModel,_I:hpicfSlotStatsModuleSerialNum,_J:hpicfSlotStatsModuleCpuStatCurrentPercent,_K:hpicfSlotStatsModuleCpuStatAveragePercent,_L:hpicfSlotStatsModuleCpuStatUpdateFrequency,'hpicfSlotStatsConformance':hpicfSlotStatsConformance,'hpicfSlotStatsGroups':hpicfSlotStatsGroups,_E:hpicfSlotStatsGroup,'hpicfSlotStatsCompliances':hpicfSlotStatsCompliances,'hpicfSlotStatsFullCompliance1':hpicfSlotStatsFullCompliance1,'hpicfModuleSlotStatsReadOnlyCompliance1':hpicfModuleSlotStatsReadOnlyCompliance1})