_G='cucsSolPolicyInstanceId'
_F='cucsSolIfInstanceId'
_E='cucsSolConfigInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-SOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsPolicyPolicyOwner,CucsSolAdminState,CucsSolSpeed=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsPolicyPolicyOwner','CucsSolAdminState','CucsSolSpeed')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsSolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,43))
_CucsSolConfigTable_Object=MibTable
cucsSolConfigTable=_CucsSolConfigTable_Object((1,3,6,1,4,1,9,9,719,1,43,1))
if mibBuilder.loadTexts:cucsSolConfigTable.setStatus(_A)
_CucsSolConfigEntry_Object=MibTableRow
cucsSolConfigEntry=_CucsSolConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,43,1,1))
cucsSolConfigEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsSolConfigEntry.setStatus(_A)
_CucsSolConfigInstanceId_Type=CucsManagedObjectId
_CucsSolConfigInstanceId_Object=MibTableColumn
cucsSolConfigInstanceId=_CucsSolConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,1),_CucsSolConfigInstanceId_Type())
cucsSolConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSolConfigInstanceId.setStatus(_A)
_CucsSolConfigDn_Type=CucsManagedObjectDn
_CucsSolConfigDn_Object=MibTableColumn
cucsSolConfigDn=_CucsSolConfigDn_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,2),_CucsSolConfigDn_Type())
cucsSolConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigDn.setStatus(_A)
_CucsSolConfigRn_Type=SnmpAdminString
_CucsSolConfigRn_Object=MibTableColumn
cucsSolConfigRn=_CucsSolConfigRn_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,3),_CucsSolConfigRn_Type())
cucsSolConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigRn.setStatus(_A)
_CucsSolConfigAdminState_Type=CucsSolAdminState
_CucsSolConfigAdminState_Object=MibTableColumn
cucsSolConfigAdminState=_CucsSolConfigAdminState_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,4),_CucsSolConfigAdminState_Type())
cucsSolConfigAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigAdminState.setStatus(_A)
_CucsSolConfigDescr_Type=SnmpAdminString
_CucsSolConfigDescr_Object=MibTableColumn
cucsSolConfigDescr=_CucsSolConfigDescr_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,5),_CucsSolConfigDescr_Type())
cucsSolConfigDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigDescr.setStatus(_A)
_CucsSolConfigIntId_Type=SnmpAdminString
_CucsSolConfigIntId_Object=MibTableColumn
cucsSolConfigIntId=_CucsSolConfigIntId_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,6),_CucsSolConfigIntId_Type())
cucsSolConfigIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigIntId.setStatus(_A)
_CucsSolConfigName_Type=SnmpAdminString
_CucsSolConfigName_Object=MibTableColumn
cucsSolConfigName=_CucsSolConfigName_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,7),_CucsSolConfigName_Type())
cucsSolConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigName.setStatus(_A)
_CucsSolConfigSpeed_Type=CucsSolSpeed
_CucsSolConfigSpeed_Object=MibTableColumn
cucsSolConfigSpeed=_CucsSolConfigSpeed_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,8),_CucsSolConfigSpeed_Type())
cucsSolConfigSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigSpeed.setStatus(_A)
_CucsSolConfigPolicyLevel_Type=Gauge32
_CucsSolConfigPolicyLevel_Object=MibTableColumn
cucsSolConfigPolicyLevel=_CucsSolConfigPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,9),_CucsSolConfigPolicyLevel_Type())
cucsSolConfigPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigPolicyLevel.setStatus(_A)
_CucsSolConfigPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsSolConfigPolicyOwner_Object=MibTableColumn
cucsSolConfigPolicyOwner=_CucsSolConfigPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,43,1,1,10),_CucsSolConfigPolicyOwner_Type())
cucsSolConfigPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolConfigPolicyOwner.setStatus(_A)
_CucsSolIfTable_Object=MibTable
cucsSolIfTable=_CucsSolIfTable_Object((1,3,6,1,4,1,9,9,719,1,43,2))
if mibBuilder.loadTexts:cucsSolIfTable.setStatus(_A)
_CucsSolIfEntry_Object=MibTableRow
cucsSolIfEntry=_CucsSolIfEntry_Object((1,3,6,1,4,1,9,9,719,1,43,2,1))
cucsSolIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsSolIfEntry.setStatus(_A)
_CucsSolIfInstanceId_Type=CucsManagedObjectId
_CucsSolIfInstanceId_Object=MibTableColumn
cucsSolIfInstanceId=_CucsSolIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,1),_CucsSolIfInstanceId_Type())
cucsSolIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSolIfInstanceId.setStatus(_A)
_CucsSolIfDn_Type=CucsManagedObjectDn
_CucsSolIfDn_Object=MibTableColumn
cucsSolIfDn=_CucsSolIfDn_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,2),_CucsSolIfDn_Type())
cucsSolIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfDn.setStatus(_A)
_CucsSolIfRn_Type=SnmpAdminString
_CucsSolIfRn_Object=MibTableColumn
cucsSolIfRn=_CucsSolIfRn_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,3),_CucsSolIfRn_Type())
cucsSolIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfRn.setStatus(_A)
_CucsSolIfAdminState_Type=CucsSolAdminState
_CucsSolIfAdminState_Object=MibTableColumn
cucsSolIfAdminState=_CucsSolIfAdminState_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,4),_CucsSolIfAdminState_Type())
cucsSolIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfAdminState.setStatus(_A)
_CucsSolIfDescr_Type=SnmpAdminString
_CucsSolIfDescr_Object=MibTableColumn
cucsSolIfDescr=_CucsSolIfDescr_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,5),_CucsSolIfDescr_Type())
cucsSolIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfDescr.setStatus(_A)
_CucsSolIfIntId_Type=SnmpAdminString
_CucsSolIfIntId_Object=MibTableColumn
cucsSolIfIntId=_CucsSolIfIntId_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,6),_CucsSolIfIntId_Type())
cucsSolIfIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfIntId.setStatus(_A)
_CucsSolIfName_Type=SnmpAdminString
_CucsSolIfName_Object=MibTableColumn
cucsSolIfName=_CucsSolIfName_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,7),_CucsSolIfName_Type())
cucsSolIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfName.setStatus(_A)
_CucsSolIfSpeed_Type=CucsSolSpeed
_CucsSolIfSpeed_Object=MibTableColumn
cucsSolIfSpeed=_CucsSolIfSpeed_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,8),_CucsSolIfSpeed_Type())
cucsSolIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfSpeed.setStatus(_A)
_CucsSolIfPolicyLevel_Type=Gauge32
_CucsSolIfPolicyLevel_Object=MibTableColumn
cucsSolIfPolicyLevel=_CucsSolIfPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,9),_CucsSolIfPolicyLevel_Type())
cucsSolIfPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfPolicyLevel.setStatus(_A)
_CucsSolIfPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsSolIfPolicyOwner_Object=MibTableColumn
cucsSolIfPolicyOwner=_CucsSolIfPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,43,2,1,10),_CucsSolIfPolicyOwner_Type())
cucsSolIfPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolIfPolicyOwner.setStatus(_A)
_CucsSolPolicyTable_Object=MibTable
cucsSolPolicyTable=_CucsSolPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,43,3))
if mibBuilder.loadTexts:cucsSolPolicyTable.setStatus(_A)
_CucsSolPolicyEntry_Object=MibTableRow
cucsSolPolicyEntry=_CucsSolPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,43,3,1))
cucsSolPolicyEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsSolPolicyEntry.setStatus(_A)
_CucsSolPolicyInstanceId_Type=CucsManagedObjectId
_CucsSolPolicyInstanceId_Object=MibTableColumn
cucsSolPolicyInstanceId=_CucsSolPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,1),_CucsSolPolicyInstanceId_Type())
cucsSolPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSolPolicyInstanceId.setStatus(_A)
_CucsSolPolicyDn_Type=CucsManagedObjectDn
_CucsSolPolicyDn_Object=MibTableColumn
cucsSolPolicyDn=_CucsSolPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,2),_CucsSolPolicyDn_Type())
cucsSolPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyDn.setStatus(_A)
_CucsSolPolicyRn_Type=SnmpAdminString
_CucsSolPolicyRn_Object=MibTableColumn
cucsSolPolicyRn=_CucsSolPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,3),_CucsSolPolicyRn_Type())
cucsSolPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyRn.setStatus(_A)
_CucsSolPolicyAdminState_Type=CucsSolAdminState
_CucsSolPolicyAdminState_Object=MibTableColumn
cucsSolPolicyAdminState=_CucsSolPolicyAdminState_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,4),_CucsSolPolicyAdminState_Type())
cucsSolPolicyAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyAdminState.setStatus(_A)
_CucsSolPolicyDescr_Type=SnmpAdminString
_CucsSolPolicyDescr_Object=MibTableColumn
cucsSolPolicyDescr=_CucsSolPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,5),_CucsSolPolicyDescr_Type())
cucsSolPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyDescr.setStatus(_A)
_CucsSolPolicyIntId_Type=SnmpAdminString
_CucsSolPolicyIntId_Object=MibTableColumn
cucsSolPolicyIntId=_CucsSolPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,6),_CucsSolPolicyIntId_Type())
cucsSolPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyIntId.setStatus(_A)
_CucsSolPolicyName_Type=SnmpAdminString
_CucsSolPolicyName_Object=MibTableColumn
cucsSolPolicyName=_CucsSolPolicyName_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,7),_CucsSolPolicyName_Type())
cucsSolPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyName.setStatus(_A)
_CucsSolPolicySpeed_Type=CucsSolSpeed
_CucsSolPolicySpeed_Object=MibTableColumn
cucsSolPolicySpeed=_CucsSolPolicySpeed_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,8),_CucsSolPolicySpeed_Type())
cucsSolPolicySpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicySpeed.setStatus(_A)
_CucsSolPolicyPolicyLevel_Type=Gauge32
_CucsSolPolicyPolicyLevel_Object=MibTableColumn
cucsSolPolicyPolicyLevel=_CucsSolPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,9),_CucsSolPolicyPolicyLevel_Type())
cucsSolPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyPolicyLevel.setStatus(_A)
_CucsSolPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsSolPolicyPolicyOwner_Object=MibTableColumn
cucsSolPolicyPolicyOwner=_CucsSolPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,10),_CucsSolPolicyPolicyOwner_Type())
cucsSolPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyPolicyOwner.setStatus(_A)
_CucsSolPolicyPropAcl_Type=Unsigned64
_CucsSolPolicyPropAcl_Object=MibTableColumn
cucsSolPolicyPropAcl=_CucsSolPolicyPropAcl_Object((1,3,6,1,4,1,9,9,719,1,43,3,1,11),_CucsSolPolicyPropAcl_Type())
cucsSolPolicyPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSolPolicyPropAcl.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsSolObjects':cucsSolObjects,'cucsSolConfigTable':cucsSolConfigTable,'cucsSolConfigEntry':cucsSolConfigEntry,_E:cucsSolConfigInstanceId,'cucsSolConfigDn':cucsSolConfigDn,'cucsSolConfigRn':cucsSolConfigRn,'cucsSolConfigAdminState':cucsSolConfigAdminState,'cucsSolConfigDescr':cucsSolConfigDescr,'cucsSolConfigIntId':cucsSolConfigIntId,'cucsSolConfigName':cucsSolConfigName,'cucsSolConfigSpeed':cucsSolConfigSpeed,'cucsSolConfigPolicyLevel':cucsSolConfigPolicyLevel,'cucsSolConfigPolicyOwner':cucsSolConfigPolicyOwner,'cucsSolIfTable':cucsSolIfTable,'cucsSolIfEntry':cucsSolIfEntry,_F:cucsSolIfInstanceId,'cucsSolIfDn':cucsSolIfDn,'cucsSolIfRn':cucsSolIfRn,'cucsSolIfAdminState':cucsSolIfAdminState,'cucsSolIfDescr':cucsSolIfDescr,'cucsSolIfIntId':cucsSolIfIntId,'cucsSolIfName':cucsSolIfName,'cucsSolIfSpeed':cucsSolIfSpeed,'cucsSolIfPolicyLevel':cucsSolIfPolicyLevel,'cucsSolIfPolicyOwner':cucsSolIfPolicyOwner,'cucsSolPolicyTable':cucsSolPolicyTable,'cucsSolPolicyEntry':cucsSolPolicyEntry,_G:cucsSolPolicyInstanceId,'cucsSolPolicyDn':cucsSolPolicyDn,'cucsSolPolicyRn':cucsSolPolicyRn,'cucsSolPolicyAdminState':cucsSolPolicyAdminState,'cucsSolPolicyDescr':cucsSolPolicyDescr,'cucsSolPolicyIntId':cucsSolPolicyIntId,'cucsSolPolicyName':cucsSolPolicyName,'cucsSolPolicySpeed':cucsSolPolicySpeed,'cucsSolPolicyPolicyLevel':cucsSolPolicyPolicyLevel,'cucsSolPolicyPolicyOwner':cucsSolPolicyPolicyOwner,'cucsSolPolicyPropAcl':cucsSolPolicyPropAcl})