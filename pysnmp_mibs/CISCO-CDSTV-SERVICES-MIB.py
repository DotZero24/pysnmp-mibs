_P='ciscoCdstvServicesMIBNotifEnableObjectGroup'
_O='ciscoCdstvServicesMIBNotificationGroup'
_N='ciscoCdstvServicesMIBMainObjectGroup'
_M='cdstvServiceDown'
_L='cdstvServiceUp'
_K='cdstvServiceDownNotifEnable'
_J='cdstvServiceUpNotifEnable'
_I='cdstvServiceStatus'
_H='read-write'
_G='read-only'
_F='cdstvServicesMonitorIndex'
_E='Unsigned32'
_D='Integer32'
_C='cdstvServiceName'
_B='CISCO-CDSTV-SERVICES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoCdstvServicesMIB=ModuleIdentity((1,3,6,1,4,1,9,9,729))
if mibBuilder.loadTexts:ciscoCdstvServicesMIB.setRevisions(('2010-03-29 00:00',))
_CiscoCdstvServicesMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvServicesMIBNotifs=_CiscoCdstvServicesMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,729,0))
_CiscoCdstvServicesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvServicesMIBObjects=_CiscoCdstvServicesMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,729,1))
_CdstvServicesMonitorTable_Object=MibTable
cdstvServicesMonitorTable=_CdstvServicesMonitorTable_Object((1,3,6,1,4,1,9,9,729,1,1))
if mibBuilder.loadTexts:cdstvServicesMonitorTable.setStatus(_A)
_CdstvServicesMonitorTableEntry_Object=MibTableRow
cdstvServicesMonitorTableEntry=_CdstvServicesMonitorTableEntry_Object((1,3,6,1,4,1,9,9,729,1,1,1))
cdstvServicesMonitorTableEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cdstvServicesMonitorTableEntry.setStatus(_A)
class _CdstvServicesMonitorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdstvServicesMonitorIndex_Type.__name__=_E
_CdstvServicesMonitorIndex_Object=MibTableColumn
cdstvServicesMonitorIndex=_CdstvServicesMonitorIndex_Object((1,3,6,1,4,1,9,9,729,1,1,1,1),_CdstvServicesMonitorIndex_Type())
cdstvServicesMonitorIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cdstvServicesMonitorIndex.setStatus(_A)
_CdstvServiceName_Type=SnmpAdminString
_CdstvServiceName_Object=MibTableColumn
cdstvServiceName=_CdstvServiceName_Object((1,3,6,1,4,1,9,9,729,1,1,1,2),_CdstvServiceName_Type())
cdstvServiceName.setMaxAccess(_G)
if mibBuilder.loadTexts:cdstvServiceName.setStatus(_A)
class _CdstvServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CdstvServiceStatus_Type.__name__=_D
_CdstvServiceStatus_Object=MibTableColumn
cdstvServiceStatus=_CdstvServiceStatus_Object((1,3,6,1,4,1,9,9,729,1,1,1,3),_CdstvServiceStatus_Type())
cdstvServiceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cdstvServiceStatus.setStatus(_A)
_CdstvServiceTrapsEnable_ObjectIdentity=ObjectIdentity
cdstvServiceTrapsEnable=_CdstvServiceTrapsEnable_ObjectIdentity((1,3,6,1,4,1,9,9,729,1,2))
_CdstvServiceUpNotifEnable_Type=TruthValue
_CdstvServiceUpNotifEnable_Object=MibScalar
cdstvServiceUpNotifEnable=_CdstvServiceUpNotifEnable_Object((1,3,6,1,4,1,9,9,729,1,2,1),_CdstvServiceUpNotifEnable_Type())
cdstvServiceUpNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cdstvServiceUpNotifEnable.setStatus(_A)
_CdstvServiceDownNotifEnable_Type=TruthValue
_CdstvServiceDownNotifEnable_Object=MibScalar
cdstvServiceDownNotifEnable=_CdstvServiceDownNotifEnable_Object((1,3,6,1,4,1,9,9,729,1,2,2),_CdstvServiceDownNotifEnable_Type())
cdstvServiceDownNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cdstvServiceDownNotifEnable.setStatus(_A)
_CiscoCdstvServicesMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvServicesMIBConform=_CiscoCdstvServicesMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,729,2))
_CiscoCdstvServicesMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvServicesMIBCompliances=_CiscoCdstvServicesMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,729,2,1))
_CiscoCdstvServicesMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvServicesMIBGroups=_CiscoCdstvServicesMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,729,2,2))
ciscoCdstvServicesMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,729,2,2,1))
ciscoCdstvServicesMIBMainObjectGroup.setObjects(*((_B,_C),(_B,_I)))
if mibBuilder.loadTexts:ciscoCdstvServicesMIBMainObjectGroup.setStatus(_A)
ciscoCdstvServicesMIBNotifEnableObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,729,2,2,3))
ciscoCdstvServicesMIBNotifEnableObjectGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoCdstvServicesMIBNotifEnableObjectGroup.setStatus(_A)
cdstvServiceUp=NotificationType((1,3,6,1,4,1,9,9,729,0,1))
cdstvServiceUp.setObjects((_B,_C))
if mibBuilder.loadTexts:cdstvServiceUp.setStatus(_A)
cdstvServiceDown=NotificationType((1,3,6,1,4,1,9,9,729,0,2))
cdstvServiceDown.setObjects((_B,_C))
if mibBuilder.loadTexts:cdstvServiceDown.setStatus(_A)
ciscoCdstvServicesMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,729,2,2,2))
ciscoCdstvServicesMIBNotificationGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoCdstvServicesMIBNotificationGroup.setStatus(_A)
ciscoCdstvServicesMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,729,2,1,1))
ciscoCdstvServicesMIBCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoCdstvServicesMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdstvServicesMIB':ciscoCdstvServicesMIB,'ciscoCdstvServicesMIBNotifs':ciscoCdstvServicesMIBNotifs,_L:cdstvServiceUp,_M:cdstvServiceDown,'ciscoCdstvServicesMIBObjects':ciscoCdstvServicesMIBObjects,'cdstvServicesMonitorTable':cdstvServicesMonitorTable,'cdstvServicesMonitorTableEntry':cdstvServicesMonitorTableEntry,_F:cdstvServicesMonitorIndex,_C:cdstvServiceName,_I:cdstvServiceStatus,'cdstvServiceTrapsEnable':cdstvServiceTrapsEnable,_J:cdstvServiceUpNotifEnable,_K:cdstvServiceDownNotifEnable,'ciscoCdstvServicesMIBConform':ciscoCdstvServicesMIBConform,'ciscoCdstvServicesMIBCompliances':ciscoCdstvServicesMIBCompliances,'ciscoCdstvServicesMIBCompliance':ciscoCdstvServicesMIBCompliance,'ciscoCdstvServicesMIBGroups':ciscoCdstvServicesMIBGroups,_N:ciscoCdstvServicesMIBMainObjectGroup,_O:ciscoCdstvServicesMIBNotificationGroup,_P:ciscoCdstvServicesMIBNotifEnableObjectGroup})