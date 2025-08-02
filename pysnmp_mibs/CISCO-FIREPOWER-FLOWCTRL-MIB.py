_F='cfprFlowctrlItemInstanceId'
_E='not-accessible'
_D='cfprFlowctrlDefinitionInstanceId'
_C='CISCO-FIREPOWER-FLOWCTRL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprFlowctrlFlowControlRx,CfprFlowctrlFlowControlTx,CfprFlowctrlPriorityPause,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprFlowctrlFlowControlRx','CfprFlowctrlFlowControlTx','CfprFlowctrlPriorityPause','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprFlowctrlObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,31))
_CfprFlowctrlDefinitionTable_Object=MibTable
cfprFlowctrlDefinitionTable=_CfprFlowctrlDefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,31,1))
if mibBuilder.loadTexts:cfprFlowctrlDefinitionTable.setStatus(_A)
_CfprFlowctrlDefinitionEntry_Object=MibTableRow
cfprFlowctrlDefinitionEntry=_CfprFlowctrlDefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,31,1,1))
cfprFlowctrlDefinitionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprFlowctrlDefinitionEntry.setStatus(_A)
_CfprFlowctrlDefinitionInstanceId_Type=CfprManagedObjectId
_CfprFlowctrlDefinitionInstanceId_Object=MibTableColumn
cfprFlowctrlDefinitionInstanceId=_CfprFlowctrlDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,1),_CfprFlowctrlDefinitionInstanceId_Type())
cfprFlowctrlDefinitionInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionInstanceId.setStatus(_A)
_CfprFlowctrlDefinitionDn_Type=CfprManagedObjectDn
_CfprFlowctrlDefinitionDn_Object=MibTableColumn
cfprFlowctrlDefinitionDn=_CfprFlowctrlDefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,2),_CfprFlowctrlDefinitionDn_Type())
cfprFlowctrlDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionDn.setStatus(_A)
_CfprFlowctrlDefinitionRn_Type=SnmpAdminString
_CfprFlowctrlDefinitionRn_Object=MibTableColumn
cfprFlowctrlDefinitionRn=_CfprFlowctrlDefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,3),_CfprFlowctrlDefinitionRn_Type())
cfprFlowctrlDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionRn.setStatus(_A)
_CfprFlowctrlDefinitionDescr_Type=SnmpAdminString
_CfprFlowctrlDefinitionDescr_Object=MibTableColumn
cfprFlowctrlDefinitionDescr=_CfprFlowctrlDefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,4),_CfprFlowctrlDefinitionDescr_Type())
cfprFlowctrlDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionDescr.setStatus(_A)
_CfprFlowctrlDefinitionIntId_Type=SnmpAdminString
_CfprFlowctrlDefinitionIntId_Object=MibTableColumn
cfprFlowctrlDefinitionIntId=_CfprFlowctrlDefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,5),_CfprFlowctrlDefinitionIntId_Type())
cfprFlowctrlDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionIntId.setStatus(_A)
_CfprFlowctrlDefinitionName_Type=SnmpAdminString
_CfprFlowctrlDefinitionName_Object=MibTableColumn
cfprFlowctrlDefinitionName=_CfprFlowctrlDefinitionName_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,6),_CfprFlowctrlDefinitionName_Type())
cfprFlowctrlDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionName.setStatus(_A)
_CfprFlowctrlDefinitionPolicyLevel_Type=Gauge32
_CfprFlowctrlDefinitionPolicyLevel_Object=MibTableColumn
cfprFlowctrlDefinitionPolicyLevel=_CfprFlowctrlDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,7),_CfprFlowctrlDefinitionPolicyLevel_Type())
cfprFlowctrlDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionPolicyLevel.setStatus(_A)
_CfprFlowctrlDefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprFlowctrlDefinitionPolicyOwner_Object=MibTableColumn
cfprFlowctrlDefinitionPolicyOwner=_CfprFlowctrlDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,31,1,1,8),_CfprFlowctrlDefinitionPolicyOwner_Type())
cfprFlowctrlDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlDefinitionPolicyOwner.setStatus(_A)
_CfprFlowctrlItemTable_Object=MibTable
cfprFlowctrlItemTable=_CfprFlowctrlItemTable_Object((1,3,6,1,4,1,9,9,826,1,31,2))
if mibBuilder.loadTexts:cfprFlowctrlItemTable.setStatus(_A)
_CfprFlowctrlItemEntry_Object=MibTableRow
cfprFlowctrlItemEntry=_CfprFlowctrlItemEntry_Object((1,3,6,1,4,1,9,9,826,1,31,2,1))
cfprFlowctrlItemEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprFlowctrlItemEntry.setStatus(_A)
_CfprFlowctrlItemInstanceId_Type=CfprManagedObjectId
_CfprFlowctrlItemInstanceId_Object=MibTableColumn
cfprFlowctrlItemInstanceId=_CfprFlowctrlItemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,1),_CfprFlowctrlItemInstanceId_Type())
cfprFlowctrlItemInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprFlowctrlItemInstanceId.setStatus(_A)
_CfprFlowctrlItemDn_Type=CfprManagedObjectDn
_CfprFlowctrlItemDn_Object=MibTableColumn
cfprFlowctrlItemDn=_CfprFlowctrlItemDn_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,2),_CfprFlowctrlItemDn_Type())
cfprFlowctrlItemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemDn.setStatus(_A)
_CfprFlowctrlItemRn_Type=SnmpAdminString
_CfprFlowctrlItemRn_Object=MibTableColumn
cfprFlowctrlItemRn=_CfprFlowctrlItemRn_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,3),_CfprFlowctrlItemRn_Type())
cfprFlowctrlItemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemRn.setStatus(_A)
_CfprFlowctrlItemName_Type=SnmpAdminString
_CfprFlowctrlItemName_Object=MibTableColumn
cfprFlowctrlItemName=_CfprFlowctrlItemName_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,4),_CfprFlowctrlItemName_Type())
cfprFlowctrlItemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemName.setStatus(_A)
_CfprFlowctrlItemPrio_Type=CfprFlowctrlPriorityPause
_CfprFlowctrlItemPrio_Object=MibTableColumn
cfprFlowctrlItemPrio=_CfprFlowctrlItemPrio_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,5),_CfprFlowctrlItemPrio_Type())
cfprFlowctrlItemPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemPrio.setStatus(_A)
_CfprFlowctrlItemRcv_Type=CfprFlowctrlFlowControlRx
_CfprFlowctrlItemRcv_Object=MibTableColumn
cfprFlowctrlItemRcv=_CfprFlowctrlItemRcv_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,6),_CfprFlowctrlItemRcv_Type())
cfprFlowctrlItemRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemRcv.setStatus(_A)
_CfprFlowctrlItemSnd_Type=CfprFlowctrlFlowControlTx
_CfprFlowctrlItemSnd_Object=MibTableColumn
cfprFlowctrlItemSnd=_CfprFlowctrlItemSnd_Object((1,3,6,1,4,1,9,9,826,1,31,2,1,7),_CfprFlowctrlItemSnd_Type())
cfprFlowctrlItemSnd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFlowctrlItemSnd.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprFlowctrlObjects':cfprFlowctrlObjects,'cfprFlowctrlDefinitionTable':cfprFlowctrlDefinitionTable,'cfprFlowctrlDefinitionEntry':cfprFlowctrlDefinitionEntry,_D:cfprFlowctrlDefinitionInstanceId,'cfprFlowctrlDefinitionDn':cfprFlowctrlDefinitionDn,'cfprFlowctrlDefinitionRn':cfprFlowctrlDefinitionRn,'cfprFlowctrlDefinitionDescr':cfprFlowctrlDefinitionDescr,'cfprFlowctrlDefinitionIntId':cfprFlowctrlDefinitionIntId,'cfprFlowctrlDefinitionName':cfprFlowctrlDefinitionName,'cfprFlowctrlDefinitionPolicyLevel':cfprFlowctrlDefinitionPolicyLevel,'cfprFlowctrlDefinitionPolicyOwner':cfprFlowctrlDefinitionPolicyOwner,'cfprFlowctrlItemTable':cfprFlowctrlItemTable,'cfprFlowctrlItemEntry':cfprFlowctrlItemEntry,_F:cfprFlowctrlItemInstanceId,'cfprFlowctrlItemDn':cfprFlowctrlItemDn,'cfprFlowctrlItemRn':cfprFlowctrlItemRn,'cfprFlowctrlItemName':cfprFlowctrlItemName,'cfprFlowctrlItemPrio':cfprFlowctrlItemPrio,'cfprFlowctrlItemRcv':cfprFlowctrlItemRcv,'cfprFlowctrlItemSnd':cfprFlowctrlItemSnd})