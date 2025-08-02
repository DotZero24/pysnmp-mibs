_D='cfprFsmStatusInstanceId'
_C='CISCO-FIREPOWER-FSM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprFsmFsmStageStatus,=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprFsmFsmStageStatus')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprFsmObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,32))
_CfprFsmStatusTable_Object=MibTable
cfprFsmStatusTable=_CfprFsmStatusTable_Object((1,3,6,1,4,1,9,9,826,1,32,1))
if mibBuilder.loadTexts:cfprFsmStatusTable.setStatus(_A)
_CfprFsmStatusEntry_Object=MibTableRow
cfprFsmStatusEntry=_CfprFsmStatusEntry_Object((1,3,6,1,4,1,9,9,826,1,32,1,1))
cfprFsmStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprFsmStatusEntry.setStatus(_A)
_CfprFsmStatusInstanceId_Type=CfprManagedObjectId
_CfprFsmStatusInstanceId_Object=MibTableColumn
cfprFsmStatusInstanceId=_CfprFsmStatusInstanceId_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,1),_CfprFsmStatusInstanceId_Type())
cfprFsmStatusInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfprFsmStatusInstanceId.setStatus(_A)
_CfprFsmStatusDn_Type=CfprManagedObjectDn
_CfprFsmStatusDn_Object=MibTableColumn
cfprFsmStatusDn=_CfprFsmStatusDn_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,2),_CfprFsmStatusDn_Type())
cfprFsmStatusDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusDn.setStatus(_A)
_CfprFsmStatusRn_Type=SnmpAdminString
_CfprFsmStatusRn_Object=MibTableColumn
cfprFsmStatusRn=_CfprFsmStatusRn_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,3),_CfprFsmStatusRn_Type())
cfprFsmStatusRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusRn.setStatus(_A)
_CfprFsmStatusConvertedEpRef_Type=SnmpAdminString
_CfprFsmStatusConvertedEpRef_Object=MibTableColumn
cfprFsmStatusConvertedEpRef=_CfprFsmStatusConvertedEpRef_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,4),_CfprFsmStatusConvertedEpRef_Type())
cfprFsmStatusConvertedEpRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusConvertedEpRef.setStatus(_A)
_CfprFsmStatusDescr_Type=SnmpAdminString
_CfprFsmStatusDescr_Object=MibTableColumn
cfprFsmStatusDescr=_CfprFsmStatusDescr_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,5),_CfprFsmStatusDescr_Type())
cfprFsmStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusDescr.setStatus(_A)
_CfprFsmStatusName_Type=SnmpAdminString
_CfprFsmStatusName_Object=MibTableColumn
cfprFsmStatusName=_CfprFsmStatusName_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,6),_CfprFsmStatusName_Type())
cfprFsmStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusName.setStatus(_A)
_CfprFsmStatusObjectClassName_Type=SnmpAdminString
_CfprFsmStatusObjectClassName_Object=MibTableColumn
cfprFsmStatusObjectClassName=_CfprFsmStatusObjectClassName_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,7),_CfprFsmStatusObjectClassName_Type())
cfprFsmStatusObjectClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusObjectClassName.setStatus(_A)
_CfprFsmStatusRemoteEpRef_Type=SnmpAdminString
_CfprFsmStatusRemoteEpRef_Object=MibTableColumn
cfprFsmStatusRemoteEpRef=_CfprFsmStatusRemoteEpRef_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,8),_CfprFsmStatusRemoteEpRef_Type())
cfprFsmStatusRemoteEpRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusRemoteEpRef.setStatus(_A)
_CfprFsmStatusState_Type=CfprFsmFsmStageStatus
_CfprFsmStatusState_Object=MibTableColumn
cfprFsmStatusState=_CfprFsmStatusState_Object((1,3,6,1,4,1,9,9,826,1,32,1,1,9),_CfprFsmStatusState_Type())
cfprFsmStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFsmStatusState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprFsmObjects':cfprFsmObjects,'cfprFsmStatusTable':cfprFsmStatusTable,'cfprFsmStatusEntry':cfprFsmStatusEntry,_D:cfprFsmStatusInstanceId,'cfprFsmStatusDn':cfprFsmStatusDn,'cfprFsmStatusRn':cfprFsmStatusRn,'cfprFsmStatusConvertedEpRef':cfprFsmStatusConvertedEpRef,'cfprFsmStatusDescr':cfprFsmStatusDescr,'cfprFsmStatusName':cfprFsmStatusName,'cfprFsmStatusObjectClassName':cfprFsmStatusObjectClassName,'cfprFsmStatusRemoteEpRef':cfprFsmStatusRemoteEpRef,'cfprFsmStatusState':cfprFsmStatusState})