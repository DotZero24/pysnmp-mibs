_I='bcsiModuleMemUtilizationGroup'
_H='bcsiModuleMemUtil100thPercent'
_G='bcsiModuleMemAvailable'
_F='bcsiModuleMemTotal'
_E='kilo Bytes'
_D='read-only'
_C='bcsiModuleMemUtilSlotNum'
_B='BROCADE-MODULE-MEM-UTIL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brocadeModuleMemUtilMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,13))
if mibBuilder.loadTexts:brocadeModuleMemUtilMIB.setRevisions(('2018-05-29 12:00','2016-11-25 00:00'))
_BcsiModuleMemUtilNotifications_ObjectIdentity=ObjectIdentity
bcsiModuleMemUtilNotifications=_BcsiModuleMemUtilNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,13,0))
_BcsiModuleMemUtilObjects_ObjectIdentity=ObjectIdentity
bcsiModuleMemUtilObjects=_BcsiModuleMemUtilObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,13,1))
_BcsiModuleMemUtilTable_Object=MibTable
bcsiModuleMemUtilTable=_BcsiModuleMemUtilTable_Object((1,3,6,1,4,1,1588,3,1,13,1,1))
if mibBuilder.loadTexts:bcsiModuleMemUtilTable.setStatus(_A)
_BcsiModuleMemUtilEntry_Object=MibTableRow
bcsiModuleMemUtilEntry=_BcsiModuleMemUtilEntry_Object((1,3,6,1,4,1,1588,3,1,13,1,1,1))
bcsiModuleMemUtilEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:bcsiModuleMemUtilEntry.setStatus(_A)
_BcsiModuleMemUtilSlotNum_Type=Integer32
_BcsiModuleMemUtilSlotNum_Object=MibTableColumn
bcsiModuleMemUtilSlotNum=_BcsiModuleMemUtilSlotNum_Object((1,3,6,1,4,1,1588,3,1,13,1,1,1,1),_BcsiModuleMemUtilSlotNum_Type())
bcsiModuleMemUtilSlotNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bcsiModuleMemUtilSlotNum.setStatus(_A)
_BcsiModuleMemTotal_Type=Unsigned32
_BcsiModuleMemTotal_Object=MibTableColumn
bcsiModuleMemTotal=_BcsiModuleMemTotal_Object((1,3,6,1,4,1,1588,3,1,13,1,1,1,2),_BcsiModuleMemTotal_Type())
bcsiModuleMemTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiModuleMemTotal.setStatus(_A)
if mibBuilder.loadTexts:bcsiModuleMemTotal.setUnits(_E)
_BcsiModuleMemAvailable_Type=Gauge32
_BcsiModuleMemAvailable_Object=MibTableColumn
bcsiModuleMemAvailable=_BcsiModuleMemAvailable_Object((1,3,6,1,4,1,1588,3,1,13,1,1,1,3),_BcsiModuleMemAvailable_Type())
bcsiModuleMemAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiModuleMemAvailable.setStatus(_A)
if mibBuilder.loadTexts:bcsiModuleMemAvailable.setUnits(_E)
_BcsiModuleMemUtil100thPercent_Type=Gauge32
_BcsiModuleMemUtil100thPercent_Object=MibTableColumn
bcsiModuleMemUtil100thPercent=_BcsiModuleMemUtil100thPercent_Object((1,3,6,1,4,1,1588,3,1,13,1,1,1,4),_BcsiModuleMemUtil100thPercent_Type())
bcsiModuleMemUtil100thPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiModuleMemUtil100thPercent.setStatus(_A)
_BcsiModuleMemUtilConformance_ObjectIdentity=ObjectIdentity
bcsiModuleMemUtilConformance=_BcsiModuleMemUtilConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,13,2))
_BcsiModuleMemUtilCompliances_ObjectIdentity=ObjectIdentity
bcsiModuleMemUtilCompliances=_BcsiModuleMemUtilCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,13,2,1))
_BcsiModuleMemUtilGroups_ObjectIdentity=ObjectIdentity
bcsiModuleMemUtilGroups=_BcsiModuleMemUtilGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,13,2,2))
bcsiModuleMemUtilizationGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,13,2,2,1))
bcsiModuleMemUtilizationGroup.setObjects(*((_B,_C),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:bcsiModuleMemUtilizationGroup.setStatus(_A)
bcsiModuleMemUtilCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,13,2,1,1))
bcsiModuleMemUtilCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:bcsiModuleMemUtilCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeModuleMemUtilMIB':brocadeModuleMemUtilMIB,'bcsiModuleMemUtilNotifications':bcsiModuleMemUtilNotifications,'bcsiModuleMemUtilObjects':bcsiModuleMemUtilObjects,'bcsiModuleMemUtilTable':bcsiModuleMemUtilTable,'bcsiModuleMemUtilEntry':bcsiModuleMemUtilEntry,_C:bcsiModuleMemUtilSlotNum,_F:bcsiModuleMemTotal,_G:bcsiModuleMemAvailable,_H:bcsiModuleMemUtil100thPercent,'bcsiModuleMemUtilConformance':bcsiModuleMemUtilConformance,'bcsiModuleMemUtilCompliances':bcsiModuleMemUtilCompliances,'bcsiModuleMemUtilCompliance':bcsiModuleMemUtilCompliance,'bcsiModuleMemUtilGroups':bcsiModuleMemUtilGroups,_I:bcsiModuleMemUtilizationGroup})