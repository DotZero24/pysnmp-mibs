_G='bcsiModuleCpuUtilizationGroup'
_F='bcsiModuleCpuUtil100thPercent'
_E='not-accessible'
_D='bcsiModuleCpuUtilInterval'
_C='bcsiModuleCpuUtilSlotNum'
_B='BROCADE-MODULE-CPU-UTIL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brocadeModuleCpuUtilMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,12))
if mibBuilder.loadTexts:brocadeModuleCpuUtilMIB.setRevisions(('2018-05-29 12:00','2016-11-25 00:00'))
_BcsiModuleCpuUtilNotifications_ObjectIdentity=ObjectIdentity
bcsiModuleCpuUtilNotifications=_BcsiModuleCpuUtilNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,12,0))
_BcsiModuleCpuUtilObjects_ObjectIdentity=ObjectIdentity
bcsiModuleCpuUtilObjects=_BcsiModuleCpuUtilObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,12,1))
_BcsiModuleCpuUtilTable_Object=MibTable
bcsiModuleCpuUtilTable=_BcsiModuleCpuUtilTable_Object((1,3,6,1,4,1,1588,3,1,12,1,1))
if mibBuilder.loadTexts:bcsiModuleCpuUtilTable.setStatus(_A)
_BcsiModuleCpuUtilEntry_Object=MibTableRow
bcsiModuleCpuUtilEntry=_BcsiModuleCpuUtilEntry_Object((1,3,6,1,4,1,1588,3,1,12,1,1,1))
bcsiModuleCpuUtilEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:bcsiModuleCpuUtilEntry.setStatus(_A)
_BcsiModuleCpuUtilSlotNum_Type=Integer32
_BcsiModuleCpuUtilSlotNum_Object=MibTableColumn
bcsiModuleCpuUtilSlotNum=_BcsiModuleCpuUtilSlotNum_Object((1,3,6,1,4,1,1588,3,1,12,1,1,1,1),_BcsiModuleCpuUtilSlotNum_Type())
bcsiModuleCpuUtilSlotNum.setMaxAccess(_E)
if mibBuilder.loadTexts:bcsiModuleCpuUtilSlotNum.setStatus(_A)
_BcsiModuleCpuUtilInterval_Type=Integer32
_BcsiModuleCpuUtilInterval_Object=MibTableColumn
bcsiModuleCpuUtilInterval=_BcsiModuleCpuUtilInterval_Object((1,3,6,1,4,1,1588,3,1,12,1,1,1,2),_BcsiModuleCpuUtilInterval_Type())
bcsiModuleCpuUtilInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bcsiModuleCpuUtilInterval.setStatus(_A)
_BcsiModuleCpuUtil100thPercent_Type=Gauge32
_BcsiModuleCpuUtil100thPercent_Object=MibTableColumn
bcsiModuleCpuUtil100thPercent=_BcsiModuleCpuUtil100thPercent_Object((1,3,6,1,4,1,1588,3,1,12,1,1,1,3),_BcsiModuleCpuUtil100thPercent_Type())
bcsiModuleCpuUtil100thPercent.setMaxAccess('read-only')
if mibBuilder.loadTexts:bcsiModuleCpuUtil100thPercent.setStatus(_A)
_BcsiModuleCpuUtilConformance_ObjectIdentity=ObjectIdentity
bcsiModuleCpuUtilConformance=_BcsiModuleCpuUtilConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,12,2))
_BcsiModuleCpuUtilCompliances_ObjectIdentity=ObjectIdentity
bcsiModuleCpuUtilCompliances=_BcsiModuleCpuUtilCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,12,2,1))
_BcsiModuleCpuUtilGroups_ObjectIdentity=ObjectIdentity
bcsiModuleCpuUtilGroups=_BcsiModuleCpuUtilGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,12,2,2))
bcsiModuleCpuUtilizationGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,12,2,2,1))
bcsiModuleCpuUtilizationGroup.setObjects(*((_B,_C),(_B,_D),(_B,_F)))
if mibBuilder.loadTexts:bcsiModuleCpuUtilizationGroup.setStatus(_A)
bcsiModuleCpuUtilCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,12,2,1,1))
bcsiModuleCpuUtilCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:bcsiModuleCpuUtilCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeModuleCpuUtilMIB':brocadeModuleCpuUtilMIB,'bcsiModuleCpuUtilNotifications':bcsiModuleCpuUtilNotifications,'bcsiModuleCpuUtilObjects':bcsiModuleCpuUtilObjects,'bcsiModuleCpuUtilTable':bcsiModuleCpuUtilTable,'bcsiModuleCpuUtilEntry':bcsiModuleCpuUtilEntry,_C:bcsiModuleCpuUtilSlotNum,_D:bcsiModuleCpuUtilInterval,_F:bcsiModuleCpuUtil100thPercent,'bcsiModuleCpuUtilConformance':bcsiModuleCpuUtilConformance,'bcsiModuleCpuUtilCompliances':bcsiModuleCpuUtilCompliances,'bcsiModuleCpuUtilCompliance':bcsiModuleCpuUtilCompliance,'bcsiModuleCpuUtilGroups':bcsiModuleCpuUtilGroups,_G:bcsiModuleCpuUtilizationGroup})