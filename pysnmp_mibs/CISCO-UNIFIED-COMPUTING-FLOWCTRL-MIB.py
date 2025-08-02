_F='cucsFlowctrlItemInstanceId'
_E='not-accessible'
_D='cucsFlowctrlDefinitionInstanceId'
_C='CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsFlowctrlConfig,CucsFlowctrlFlowControl,CucsFlowctrlPriorityPause,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsFlowctrlConfig','CucsFlowctrlFlowControl','CucsFlowctrlPriorityPause','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsFlowctrlObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,23))
_CucsFlowctrlDefinitionTable_Object=MibTable
cucsFlowctrlDefinitionTable=_CucsFlowctrlDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,23,1))
if mibBuilder.loadTexts:cucsFlowctrlDefinitionTable.setStatus(_A)
_CucsFlowctrlDefinitionEntry_Object=MibTableRow
cucsFlowctrlDefinitionEntry=_CucsFlowctrlDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,23,1,1))
cucsFlowctrlDefinitionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsFlowctrlDefinitionEntry.setStatus(_A)
_CucsFlowctrlDefinitionInstanceId_Type=CucsManagedObjectId
_CucsFlowctrlDefinitionInstanceId_Object=MibTableColumn
cucsFlowctrlDefinitionInstanceId=_CucsFlowctrlDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,1),_CucsFlowctrlDefinitionInstanceId_Type())
cucsFlowctrlDefinitionInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionInstanceId.setStatus(_A)
_CucsFlowctrlDefinitionDn_Type=CucsManagedObjectDn
_CucsFlowctrlDefinitionDn_Object=MibTableColumn
cucsFlowctrlDefinitionDn=_CucsFlowctrlDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,2),_CucsFlowctrlDefinitionDn_Type())
cucsFlowctrlDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionDn.setStatus(_A)
_CucsFlowctrlDefinitionRn_Type=SnmpAdminString
_CucsFlowctrlDefinitionRn_Object=MibTableColumn
cucsFlowctrlDefinitionRn=_CucsFlowctrlDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,3),_CucsFlowctrlDefinitionRn_Type())
cucsFlowctrlDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionRn.setStatus(_A)
_CucsFlowctrlDefinitionDescr_Type=SnmpAdminString
_CucsFlowctrlDefinitionDescr_Object=MibTableColumn
cucsFlowctrlDefinitionDescr=_CucsFlowctrlDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,4),_CucsFlowctrlDefinitionDescr_Type())
cucsFlowctrlDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionDescr.setStatus(_A)
_CucsFlowctrlDefinitionIntId_Type=SnmpAdminString
_CucsFlowctrlDefinitionIntId_Object=MibTableColumn
cucsFlowctrlDefinitionIntId=_CucsFlowctrlDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,5),_CucsFlowctrlDefinitionIntId_Type())
cucsFlowctrlDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionIntId.setStatus(_A)
_CucsFlowctrlDefinitionName_Type=SnmpAdminString
_CucsFlowctrlDefinitionName_Object=MibTableColumn
cucsFlowctrlDefinitionName=_CucsFlowctrlDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,6),_CucsFlowctrlDefinitionName_Type())
cucsFlowctrlDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionName.setStatus(_A)
_CucsFlowctrlDefinitionPolicyLevel_Type=Gauge32
_CucsFlowctrlDefinitionPolicyLevel_Object=MibTableColumn
cucsFlowctrlDefinitionPolicyLevel=_CucsFlowctrlDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,7),_CucsFlowctrlDefinitionPolicyLevel_Type())
cucsFlowctrlDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionPolicyLevel.setStatus(_A)
_CucsFlowctrlDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsFlowctrlDefinitionPolicyOwner_Object=MibTableColumn
cucsFlowctrlDefinitionPolicyOwner=_CucsFlowctrlDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,23,1,1,8),_CucsFlowctrlDefinitionPolicyOwner_Type())
cucsFlowctrlDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlDefinitionPolicyOwner.setStatus(_A)
_CucsFlowctrlItemTable_Object=MibTable
cucsFlowctrlItemTable=_CucsFlowctrlItemTable_Object((1,3,6,1,4,1,9,9,719,1,23,2))
if mibBuilder.loadTexts:cucsFlowctrlItemTable.setStatus(_A)
_CucsFlowctrlItemEntry_Object=MibTableRow
cucsFlowctrlItemEntry=_CucsFlowctrlItemEntry_Object((1,3,6,1,4,1,9,9,719,1,23,2,1))
cucsFlowctrlItemEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsFlowctrlItemEntry.setStatus(_A)
_CucsFlowctrlItemInstanceId_Type=CucsManagedObjectId
_CucsFlowctrlItemInstanceId_Object=MibTableColumn
cucsFlowctrlItemInstanceId=_CucsFlowctrlItemInstanceId_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,1),_CucsFlowctrlItemInstanceId_Type())
cucsFlowctrlItemInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsFlowctrlItemInstanceId.setStatus(_A)
_CucsFlowctrlItemDn_Type=CucsManagedObjectDn
_CucsFlowctrlItemDn_Object=MibTableColumn
cucsFlowctrlItemDn=_CucsFlowctrlItemDn_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,2),_CucsFlowctrlItemDn_Type())
cucsFlowctrlItemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemDn.setStatus(_A)
_CucsFlowctrlItemRn_Type=SnmpAdminString
_CucsFlowctrlItemRn_Object=MibTableColumn
cucsFlowctrlItemRn=_CucsFlowctrlItemRn_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,3),_CucsFlowctrlItemRn_Type())
cucsFlowctrlItemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemRn.setStatus(_A)
_CucsFlowctrlItemName_Type=SnmpAdminString
_CucsFlowctrlItemName_Object=MibTableColumn
cucsFlowctrlItemName=_CucsFlowctrlItemName_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,4),_CucsFlowctrlItemName_Type())
cucsFlowctrlItemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemName.setStatus(_A)
_CucsFlowctrlItemPrio_Type=CucsFlowctrlPriorityPause
_CucsFlowctrlItemPrio_Object=MibTableColumn
cucsFlowctrlItemPrio=_CucsFlowctrlItemPrio_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,5),_CucsFlowctrlItemPrio_Type())
cucsFlowctrlItemPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemPrio.setStatus(_A)
_CucsFlowctrlItemRcv_Type=CucsFlowctrlFlowControl
_CucsFlowctrlItemRcv_Object=MibTableColumn
cucsFlowctrlItemRcv=_CucsFlowctrlItemRcv_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,6),_CucsFlowctrlItemRcv_Type())
cucsFlowctrlItemRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemRcv.setStatus(_A)
_CucsFlowctrlItemSnd_Type=CucsFlowctrlFlowControl
_CucsFlowctrlItemSnd_Object=MibTableColumn
cucsFlowctrlItemSnd=_CucsFlowctrlItemSnd_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,7),_CucsFlowctrlItemSnd_Type())
cucsFlowctrlItemSnd.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemSnd.setStatus(_A)
_CucsFlowctrlItemConfig_Type=CucsFlowctrlConfig
_CucsFlowctrlItemConfig_Object=MibTableColumn
cucsFlowctrlItemConfig=_CucsFlowctrlItemConfig_Object((1,3,6,1,4,1,9,9,719,1,23,2,1,8),_CucsFlowctrlItemConfig_Type())
cucsFlowctrlItemConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFlowctrlItemConfig.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsFlowctrlObjects':cucsFlowctrlObjects,'cucsFlowctrlDefinitionTable':cucsFlowctrlDefinitionTable,'cucsFlowctrlDefinitionEntry':cucsFlowctrlDefinitionEntry,_D:cucsFlowctrlDefinitionInstanceId,'cucsFlowctrlDefinitionDn':cucsFlowctrlDefinitionDn,'cucsFlowctrlDefinitionRn':cucsFlowctrlDefinitionRn,'cucsFlowctrlDefinitionDescr':cucsFlowctrlDefinitionDescr,'cucsFlowctrlDefinitionIntId':cucsFlowctrlDefinitionIntId,'cucsFlowctrlDefinitionName':cucsFlowctrlDefinitionName,'cucsFlowctrlDefinitionPolicyLevel':cucsFlowctrlDefinitionPolicyLevel,'cucsFlowctrlDefinitionPolicyOwner':cucsFlowctrlDefinitionPolicyOwner,'cucsFlowctrlItemTable':cucsFlowctrlItemTable,'cucsFlowctrlItemEntry':cucsFlowctrlItemEntry,_F:cucsFlowctrlItemInstanceId,'cucsFlowctrlItemDn':cucsFlowctrlItemDn,'cucsFlowctrlItemRn':cucsFlowctrlItemRn,'cucsFlowctrlItemName':cucsFlowctrlItemName,'cucsFlowctrlItemPrio':cucsFlowctrlItemPrio,'cucsFlowctrlItemRcv':cucsFlowctrlItemRcv,'cucsFlowctrlItemSnd':cucsFlowctrlItemSnd,'cucsFlowctrlItemConfig':cucsFlowctrlItemConfig})