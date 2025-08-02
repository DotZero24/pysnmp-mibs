_G='cfprSolPolicyInstanceId'
_F='cfprSolIfInstanceId'
_E='cfprSolConfigInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-SOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprPolicyPolicyOwner,CfprSolAdminState,CfprSolSpeed=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprPolicyPolicyOwner','CfprSolAdminState','CfprSolSpeed')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprSolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,72))
_CfprSolConfigTable_Object=MibTable
cfprSolConfigTable=_CfprSolConfigTable_Object((1,3,6,1,4,1,9,9,826,1,72,1))
if mibBuilder.loadTexts:cfprSolConfigTable.setStatus(_A)
_CfprSolConfigEntry_Object=MibTableRow
cfprSolConfigEntry=_CfprSolConfigEntry_Object((1,3,6,1,4,1,9,9,826,1,72,1,1))
cfprSolConfigEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprSolConfigEntry.setStatus(_A)
_CfprSolConfigInstanceId_Type=CfprManagedObjectId
_CfprSolConfigInstanceId_Object=MibTableColumn
cfprSolConfigInstanceId=_CfprSolConfigInstanceId_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,1),_CfprSolConfigInstanceId_Type())
cfprSolConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprSolConfigInstanceId.setStatus(_A)
_CfprSolConfigDn_Type=CfprManagedObjectDn
_CfprSolConfigDn_Object=MibTableColumn
cfprSolConfigDn=_CfprSolConfigDn_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,2),_CfprSolConfigDn_Type())
cfprSolConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigDn.setStatus(_A)
_CfprSolConfigRn_Type=SnmpAdminString
_CfprSolConfigRn_Object=MibTableColumn
cfprSolConfigRn=_CfprSolConfigRn_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,3),_CfprSolConfigRn_Type())
cfprSolConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigRn.setStatus(_A)
_CfprSolConfigAdminState_Type=CfprSolAdminState
_CfprSolConfigAdminState_Object=MibTableColumn
cfprSolConfigAdminState=_CfprSolConfigAdminState_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,4),_CfprSolConfigAdminState_Type())
cfprSolConfigAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigAdminState.setStatus(_A)
_CfprSolConfigDescr_Type=SnmpAdminString
_CfprSolConfigDescr_Object=MibTableColumn
cfprSolConfigDescr=_CfprSolConfigDescr_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,5),_CfprSolConfigDescr_Type())
cfprSolConfigDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigDescr.setStatus(_A)
_CfprSolConfigIntId_Type=SnmpAdminString
_CfprSolConfigIntId_Object=MibTableColumn
cfprSolConfigIntId=_CfprSolConfigIntId_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,6),_CfprSolConfigIntId_Type())
cfprSolConfigIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigIntId.setStatus(_A)
_CfprSolConfigName_Type=SnmpAdminString
_CfprSolConfigName_Object=MibTableColumn
cfprSolConfigName=_CfprSolConfigName_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,7),_CfprSolConfigName_Type())
cfprSolConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigName.setStatus(_A)
_CfprSolConfigPolicyLevel_Type=Gauge32
_CfprSolConfigPolicyLevel_Object=MibTableColumn
cfprSolConfigPolicyLevel=_CfprSolConfigPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,8),_CfprSolConfigPolicyLevel_Type())
cfprSolConfigPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigPolicyLevel.setStatus(_A)
_CfprSolConfigPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprSolConfigPolicyOwner_Object=MibTableColumn
cfprSolConfigPolicyOwner=_CfprSolConfigPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,9),_CfprSolConfigPolicyOwner_Type())
cfprSolConfigPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigPolicyOwner.setStatus(_A)
_CfprSolConfigSpeed_Type=CfprSolSpeed
_CfprSolConfigSpeed_Object=MibTableColumn
cfprSolConfigSpeed=_CfprSolConfigSpeed_Object((1,3,6,1,4,1,9,9,826,1,72,1,1,10),_CfprSolConfigSpeed_Type())
cfprSolConfigSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolConfigSpeed.setStatus(_A)
_CfprSolIfTable_Object=MibTable
cfprSolIfTable=_CfprSolIfTable_Object((1,3,6,1,4,1,9,9,826,1,72,2))
if mibBuilder.loadTexts:cfprSolIfTable.setStatus(_A)
_CfprSolIfEntry_Object=MibTableRow
cfprSolIfEntry=_CfprSolIfEntry_Object((1,3,6,1,4,1,9,9,826,1,72,2,1))
cfprSolIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprSolIfEntry.setStatus(_A)
_CfprSolIfInstanceId_Type=CfprManagedObjectId
_CfprSolIfInstanceId_Object=MibTableColumn
cfprSolIfInstanceId=_CfprSolIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,1),_CfprSolIfInstanceId_Type())
cfprSolIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprSolIfInstanceId.setStatus(_A)
_CfprSolIfDn_Type=CfprManagedObjectDn
_CfprSolIfDn_Object=MibTableColumn
cfprSolIfDn=_CfprSolIfDn_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,2),_CfprSolIfDn_Type())
cfprSolIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfDn.setStatus(_A)
_CfprSolIfRn_Type=SnmpAdminString
_CfprSolIfRn_Object=MibTableColumn
cfprSolIfRn=_CfprSolIfRn_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,3),_CfprSolIfRn_Type())
cfprSolIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfRn.setStatus(_A)
_CfprSolIfAdminState_Type=CfprSolAdminState
_CfprSolIfAdminState_Object=MibTableColumn
cfprSolIfAdminState=_CfprSolIfAdminState_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,4),_CfprSolIfAdminState_Type())
cfprSolIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfAdminState.setStatus(_A)
_CfprSolIfDescr_Type=SnmpAdminString
_CfprSolIfDescr_Object=MibTableColumn
cfprSolIfDescr=_CfprSolIfDescr_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,5),_CfprSolIfDescr_Type())
cfprSolIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfDescr.setStatus(_A)
_CfprSolIfIntId_Type=SnmpAdminString
_CfprSolIfIntId_Object=MibTableColumn
cfprSolIfIntId=_CfprSolIfIntId_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,6),_CfprSolIfIntId_Type())
cfprSolIfIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfIntId.setStatus(_A)
_CfprSolIfName_Type=SnmpAdminString
_CfprSolIfName_Object=MibTableColumn
cfprSolIfName=_CfprSolIfName_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,7),_CfprSolIfName_Type())
cfprSolIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfName.setStatus(_A)
_CfprSolIfPolicyLevel_Type=Gauge32
_CfprSolIfPolicyLevel_Object=MibTableColumn
cfprSolIfPolicyLevel=_CfprSolIfPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,8),_CfprSolIfPolicyLevel_Type())
cfprSolIfPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfPolicyLevel.setStatus(_A)
_CfprSolIfPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprSolIfPolicyOwner_Object=MibTableColumn
cfprSolIfPolicyOwner=_CfprSolIfPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,9),_CfprSolIfPolicyOwner_Type())
cfprSolIfPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfPolicyOwner.setStatus(_A)
_CfprSolIfSpeed_Type=CfprSolSpeed
_CfprSolIfSpeed_Object=MibTableColumn
cfprSolIfSpeed=_CfprSolIfSpeed_Object((1,3,6,1,4,1,9,9,826,1,72,2,1,10),_CfprSolIfSpeed_Type())
cfprSolIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolIfSpeed.setStatus(_A)
_CfprSolPolicyTable_Object=MibTable
cfprSolPolicyTable=_CfprSolPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,72,3))
if mibBuilder.loadTexts:cfprSolPolicyTable.setStatus(_A)
_CfprSolPolicyEntry_Object=MibTableRow
cfprSolPolicyEntry=_CfprSolPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,72,3,1))
cfprSolPolicyEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprSolPolicyEntry.setStatus(_A)
_CfprSolPolicyInstanceId_Type=CfprManagedObjectId
_CfprSolPolicyInstanceId_Object=MibTableColumn
cfprSolPolicyInstanceId=_CfprSolPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,1),_CfprSolPolicyInstanceId_Type())
cfprSolPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprSolPolicyInstanceId.setStatus(_A)
_CfprSolPolicyDn_Type=CfprManagedObjectDn
_CfprSolPolicyDn_Object=MibTableColumn
cfprSolPolicyDn=_CfprSolPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,2),_CfprSolPolicyDn_Type())
cfprSolPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyDn.setStatus(_A)
_CfprSolPolicyRn_Type=SnmpAdminString
_CfprSolPolicyRn_Object=MibTableColumn
cfprSolPolicyRn=_CfprSolPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,3),_CfprSolPolicyRn_Type())
cfprSolPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyRn.setStatus(_A)
_CfprSolPolicyAdminState_Type=CfprSolAdminState
_CfprSolPolicyAdminState_Object=MibTableColumn
cfprSolPolicyAdminState=_CfprSolPolicyAdminState_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,4),_CfprSolPolicyAdminState_Type())
cfprSolPolicyAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyAdminState.setStatus(_A)
_CfprSolPolicyDescr_Type=SnmpAdminString
_CfprSolPolicyDescr_Object=MibTableColumn
cfprSolPolicyDescr=_CfprSolPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,5),_CfprSolPolicyDescr_Type())
cfprSolPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyDescr.setStatus(_A)
_CfprSolPolicyIntId_Type=SnmpAdminString
_CfprSolPolicyIntId_Object=MibTableColumn
cfprSolPolicyIntId=_CfprSolPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,6),_CfprSolPolicyIntId_Type())
cfprSolPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyIntId.setStatus(_A)
_CfprSolPolicyName_Type=SnmpAdminString
_CfprSolPolicyName_Object=MibTableColumn
cfprSolPolicyName=_CfprSolPolicyName_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,7),_CfprSolPolicyName_Type())
cfprSolPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyName.setStatus(_A)
_CfprSolPolicyPolicyLevel_Type=Gauge32
_CfprSolPolicyPolicyLevel_Object=MibTableColumn
cfprSolPolicyPolicyLevel=_CfprSolPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,8),_CfprSolPolicyPolicyLevel_Type())
cfprSolPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyPolicyLevel.setStatus(_A)
_CfprSolPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprSolPolicyPolicyOwner_Object=MibTableColumn
cfprSolPolicyPolicyOwner=_CfprSolPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,9),_CfprSolPolicyPolicyOwner_Type())
cfprSolPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicyPolicyOwner.setStatus(_A)
_CfprSolPolicySpeed_Type=CfprSolSpeed
_CfprSolPolicySpeed_Object=MibTableColumn
cfprSolPolicySpeed=_CfprSolPolicySpeed_Object((1,3,6,1,4,1,9,9,826,1,72,3,1,10),_CfprSolPolicySpeed_Type())
cfprSolPolicySpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprSolPolicySpeed.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprSolObjects':cfprSolObjects,'cfprSolConfigTable':cfprSolConfigTable,'cfprSolConfigEntry':cfprSolConfigEntry,_E:cfprSolConfigInstanceId,'cfprSolConfigDn':cfprSolConfigDn,'cfprSolConfigRn':cfprSolConfigRn,'cfprSolConfigAdminState':cfprSolConfigAdminState,'cfprSolConfigDescr':cfprSolConfigDescr,'cfprSolConfigIntId':cfprSolConfigIntId,'cfprSolConfigName':cfprSolConfigName,'cfprSolConfigPolicyLevel':cfprSolConfigPolicyLevel,'cfprSolConfigPolicyOwner':cfprSolConfigPolicyOwner,'cfprSolConfigSpeed':cfprSolConfigSpeed,'cfprSolIfTable':cfprSolIfTable,'cfprSolIfEntry':cfprSolIfEntry,_F:cfprSolIfInstanceId,'cfprSolIfDn':cfprSolIfDn,'cfprSolIfRn':cfprSolIfRn,'cfprSolIfAdminState':cfprSolIfAdminState,'cfprSolIfDescr':cfprSolIfDescr,'cfprSolIfIntId':cfprSolIfIntId,'cfprSolIfName':cfprSolIfName,'cfprSolIfPolicyLevel':cfprSolIfPolicyLevel,'cfprSolIfPolicyOwner':cfprSolIfPolicyOwner,'cfprSolIfSpeed':cfprSolIfSpeed,'cfprSolPolicyTable':cfprSolPolicyTable,'cfprSolPolicyEntry':cfprSolPolicyEntry,_G:cfprSolPolicyInstanceId,'cfprSolPolicyDn':cfprSolPolicyDn,'cfprSolPolicyRn':cfprSolPolicyRn,'cfprSolPolicyAdminState':cfprSolPolicyAdminState,'cfprSolPolicyDescr':cfprSolPolicyDescr,'cfprSolPolicyIntId':cfprSolPolicyIntId,'cfprSolPolicyName':cfprSolPolicyName,'cfprSolPolicyPolicyLevel':cfprSolPolicyPolicyLevel,'cfprSolPolicyPolicyOwner':cfprSolPolicyPolicyOwner,'cfprSolPolicySpeed':cfprSolPolicySpeed})