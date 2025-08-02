_D='cucsNwctrlDefinitionInstanceId'
_C='CISCO-UNIFIED-COMPUTING-NWCTRL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsNwctrlAdminState,CucsNwctrlLinkFailAction,CucsNwctrlRegistrationMode,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsNwctrlAdminState','CucsNwctrlLinkFailAction','CucsNwctrlRegistrationMode','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsNwctrlObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,33))
_CucsNwctrlDefinitionTable_Object=MibTable
cucsNwctrlDefinitionTable=_CucsNwctrlDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,33,1))
if mibBuilder.loadTexts:cucsNwctrlDefinitionTable.setStatus(_A)
_CucsNwctrlDefinitionEntry_Object=MibTableRow
cucsNwctrlDefinitionEntry=_CucsNwctrlDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,33,1,1))
cucsNwctrlDefinitionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsNwctrlDefinitionEntry.setStatus(_A)
_CucsNwctrlDefinitionInstanceId_Type=CucsManagedObjectId
_CucsNwctrlDefinitionInstanceId_Object=MibTableColumn
cucsNwctrlDefinitionInstanceId=_CucsNwctrlDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,1),_CucsNwctrlDefinitionInstanceId_Type())
cucsNwctrlDefinitionInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsNwctrlDefinitionInstanceId.setStatus(_A)
_CucsNwctrlDefinitionDn_Type=CucsManagedObjectDn
_CucsNwctrlDefinitionDn_Object=MibTableColumn
cucsNwctrlDefinitionDn=_CucsNwctrlDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,2),_CucsNwctrlDefinitionDn_Type())
cucsNwctrlDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionDn.setStatus(_A)
_CucsNwctrlDefinitionRn_Type=SnmpAdminString
_CucsNwctrlDefinitionRn_Object=MibTableColumn
cucsNwctrlDefinitionRn=_CucsNwctrlDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,3),_CucsNwctrlDefinitionRn_Type())
cucsNwctrlDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionRn.setStatus(_A)
_CucsNwctrlDefinitionCdp_Type=CucsNwctrlAdminState
_CucsNwctrlDefinitionCdp_Object=MibTableColumn
cucsNwctrlDefinitionCdp=_CucsNwctrlDefinitionCdp_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,4),_CucsNwctrlDefinitionCdp_Type())
cucsNwctrlDefinitionCdp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionCdp.setStatus(_A)
_CucsNwctrlDefinitionDescr_Type=SnmpAdminString
_CucsNwctrlDefinitionDescr_Object=MibTableColumn
cucsNwctrlDefinitionDescr=_CucsNwctrlDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,5),_CucsNwctrlDefinitionDescr_Type())
cucsNwctrlDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionDescr.setStatus(_A)
_CucsNwctrlDefinitionIntId_Type=SnmpAdminString
_CucsNwctrlDefinitionIntId_Object=MibTableColumn
cucsNwctrlDefinitionIntId=_CucsNwctrlDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,6),_CucsNwctrlDefinitionIntId_Type())
cucsNwctrlDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionIntId.setStatus(_A)
_CucsNwctrlDefinitionName_Type=SnmpAdminString
_CucsNwctrlDefinitionName_Object=MibTableColumn
cucsNwctrlDefinitionName=_CucsNwctrlDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,7),_CucsNwctrlDefinitionName_Type())
cucsNwctrlDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionName.setStatus(_A)
_CucsNwctrlDefinitionUplinkFailAction_Type=CucsNwctrlLinkFailAction
_CucsNwctrlDefinitionUplinkFailAction_Object=MibTableColumn
cucsNwctrlDefinitionUplinkFailAction=_CucsNwctrlDefinitionUplinkFailAction_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,8),_CucsNwctrlDefinitionUplinkFailAction_Type())
cucsNwctrlDefinitionUplinkFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionUplinkFailAction.setStatus(_A)
_CucsNwctrlDefinitionMacRegisterMode_Type=CucsNwctrlRegistrationMode
_CucsNwctrlDefinitionMacRegisterMode_Object=MibTableColumn
cucsNwctrlDefinitionMacRegisterMode=_CucsNwctrlDefinitionMacRegisterMode_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,9),_CucsNwctrlDefinitionMacRegisterMode_Type())
cucsNwctrlDefinitionMacRegisterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionMacRegisterMode.setStatus(_A)
_CucsNwctrlDefinitionPolicyLevel_Type=Gauge32
_CucsNwctrlDefinitionPolicyLevel_Object=MibTableColumn
cucsNwctrlDefinitionPolicyLevel=_CucsNwctrlDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,10),_CucsNwctrlDefinitionPolicyLevel_Type())
cucsNwctrlDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionPolicyLevel.setStatus(_A)
_CucsNwctrlDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsNwctrlDefinitionPolicyOwner_Object=MibTableColumn
cucsNwctrlDefinitionPolicyOwner=_CucsNwctrlDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,11),_CucsNwctrlDefinitionPolicyOwner_Type())
cucsNwctrlDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionPolicyOwner.setStatus(_A)
_CucsNwctrlDefinitionPropAcl_Type=Unsigned64
_CucsNwctrlDefinitionPropAcl_Object=MibTableColumn
cucsNwctrlDefinitionPropAcl=_CucsNwctrlDefinitionPropAcl_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,12),_CucsNwctrlDefinitionPropAcl_Type())
cucsNwctrlDefinitionPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionPropAcl.setStatus(_A)
_CucsNwctrlDefinitionLldpReceive_Type=CucsNwctrlAdminState
_CucsNwctrlDefinitionLldpReceive_Object=MibTableColumn
cucsNwctrlDefinitionLldpReceive=_CucsNwctrlDefinitionLldpReceive_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,13),_CucsNwctrlDefinitionLldpReceive_Type())
cucsNwctrlDefinitionLldpReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionLldpReceive.setStatus(_A)
_CucsNwctrlDefinitionLldpTransmit_Type=CucsNwctrlAdminState
_CucsNwctrlDefinitionLldpTransmit_Object=MibTableColumn
cucsNwctrlDefinitionLldpTransmit=_CucsNwctrlDefinitionLldpTransmit_Object((1,3,6,1,4,1,9,9,719,1,33,1,1,14),_CucsNwctrlDefinitionLldpTransmit_Type())
cucsNwctrlDefinitionLldpTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNwctrlDefinitionLldpTransmit.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsNwctrlObjects':cucsNwctrlObjects,'cucsNwctrlDefinitionTable':cucsNwctrlDefinitionTable,'cucsNwctrlDefinitionEntry':cucsNwctrlDefinitionEntry,_D:cucsNwctrlDefinitionInstanceId,'cucsNwctrlDefinitionDn':cucsNwctrlDefinitionDn,'cucsNwctrlDefinitionRn':cucsNwctrlDefinitionRn,'cucsNwctrlDefinitionCdp':cucsNwctrlDefinitionCdp,'cucsNwctrlDefinitionDescr':cucsNwctrlDefinitionDescr,'cucsNwctrlDefinitionIntId':cucsNwctrlDefinitionIntId,'cucsNwctrlDefinitionName':cucsNwctrlDefinitionName,'cucsNwctrlDefinitionUplinkFailAction':cucsNwctrlDefinitionUplinkFailAction,'cucsNwctrlDefinitionMacRegisterMode':cucsNwctrlDefinitionMacRegisterMode,'cucsNwctrlDefinitionPolicyLevel':cucsNwctrlDefinitionPolicyLevel,'cucsNwctrlDefinitionPolicyOwner':cucsNwctrlDefinitionPolicyOwner,'cucsNwctrlDefinitionPropAcl':cucsNwctrlDefinitionPropAcl,'cucsNwctrlDefinitionLldpReceive':cucsNwctrlDefinitionLldpReceive,'cucsNwctrlDefinitionLldpTransmit':cucsNwctrlDefinitionLldpTransmit})