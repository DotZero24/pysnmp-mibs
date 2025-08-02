_D='zyDhcpOption82ProfileName'
_C='ZYXEL-DHCP-OPTION82-PROFILE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDhcpOption82Profile=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,17))
_ZyxelDhcpOption82ProfileSetup_ObjectIdentity=ObjectIdentity
zyxelDhcpOption82ProfileSetup=_ZyxelDhcpOption82ProfileSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,17,1))
_ZyDhcpOption82ProfileMaxNumberOfProfiles_Type=Integer32
_ZyDhcpOption82ProfileMaxNumberOfProfiles_Object=MibScalar
zyDhcpOption82ProfileMaxNumberOfProfiles=_ZyDhcpOption82ProfileMaxNumberOfProfiles_Object((1,3,6,1,4,1,890,1,15,3,17,1,1),_ZyDhcpOption82ProfileMaxNumberOfProfiles_Type())
zyDhcpOption82ProfileMaxNumberOfProfiles.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyDhcpOption82ProfileMaxNumberOfProfiles.setStatus(_A)
_ZyxelDhcpOption82ProfileTable_Object=MibTable
zyxelDhcpOption82ProfileTable=_ZyxelDhcpOption82ProfileTable_Object((1,3,6,1,4,1,890,1,15,3,17,1,2))
if mibBuilder.loadTexts:zyxelDhcpOption82ProfileTable.setStatus(_A)
_ZyxelDhcpOption82ProfileEntry_Object=MibTableRow
zyxelDhcpOption82ProfileEntry=_ZyxelDhcpOption82ProfileEntry_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1))
zyxelDhcpOption82ProfileEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelDhcpOption82ProfileEntry.setStatus(_A)
_ZyDhcpOption82ProfileName_Type=DisplayString
_ZyDhcpOption82ProfileName_Object=MibTableColumn
zyDhcpOption82ProfileName=_ZyDhcpOption82ProfileName_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,1),_ZyDhcpOption82ProfileName_Type())
zyDhcpOption82ProfileName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyDhcpOption82ProfileName.setStatus(_A)
_ZyDhcpOption82ProfileCircuitIdState_Type=EnabledStatus
_ZyDhcpOption82ProfileCircuitIdState_Object=MibTableColumn
zyDhcpOption82ProfileCircuitIdState=_ZyDhcpOption82ProfileCircuitIdState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,2),_ZyDhcpOption82ProfileCircuitIdState_Type())
zyDhcpOption82ProfileCircuitIdState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileCircuitIdState.setStatus(_A)
_ZyDhcpOption82ProfileCircuitIdSlotPortState_Type=EnabledStatus
_ZyDhcpOption82ProfileCircuitIdSlotPortState_Object=MibTableColumn
zyDhcpOption82ProfileCircuitIdSlotPortState=_ZyDhcpOption82ProfileCircuitIdSlotPortState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,3),_ZyDhcpOption82ProfileCircuitIdSlotPortState_Type())
zyDhcpOption82ProfileCircuitIdSlotPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileCircuitIdSlotPortState.setStatus(_A)
_ZyDhcpOption82ProfileCircuitIdVidState_Type=EnabledStatus
_ZyDhcpOption82ProfileCircuitIdVidState_Object=MibTableColumn
zyDhcpOption82ProfileCircuitIdVidState=_ZyDhcpOption82ProfileCircuitIdVidState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,4),_ZyDhcpOption82ProfileCircuitIdVidState_Type())
zyDhcpOption82ProfileCircuitIdVidState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileCircuitIdVidState.setStatus(_A)
_ZyDhcpOption82ProfileCircuitIdHostnameState_Type=EnabledStatus
_ZyDhcpOption82ProfileCircuitIdHostnameState_Object=MibTableColumn
zyDhcpOption82ProfileCircuitIdHostnameState=_ZyDhcpOption82ProfileCircuitIdHostnameState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,5),_ZyDhcpOption82ProfileCircuitIdHostnameState_Type())
zyDhcpOption82ProfileCircuitIdHostnameState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileCircuitIdHostnameState.setStatus(_A)
_ZyDhcpOption82ProfileCircuitIdString_Type=DisplayString
_ZyDhcpOption82ProfileCircuitIdString_Object=MibTableColumn
zyDhcpOption82ProfileCircuitIdString=_ZyDhcpOption82ProfileCircuitIdString_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,6),_ZyDhcpOption82ProfileCircuitIdString_Type())
zyDhcpOption82ProfileCircuitIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileCircuitIdString.setStatus(_A)
_ZyDhcpOption82ProfileRemoteIdState_Type=EnabledStatus
_ZyDhcpOption82ProfileRemoteIdState_Object=MibTableColumn
zyDhcpOption82ProfileRemoteIdState=_ZyDhcpOption82ProfileRemoteIdState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,7),_ZyDhcpOption82ProfileRemoteIdState_Type())
zyDhcpOption82ProfileRemoteIdState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileRemoteIdState.setStatus(_A)
_ZyDhcpOption82ProfileRemoteIdMacAddressState_Type=EnabledStatus
_ZyDhcpOption82ProfileRemoteIdMacAddressState_Object=MibTableColumn
zyDhcpOption82ProfileRemoteIdMacAddressState=_ZyDhcpOption82ProfileRemoteIdMacAddressState_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,8),_ZyDhcpOption82ProfileRemoteIdMacAddressState_Type())
zyDhcpOption82ProfileRemoteIdMacAddressState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileRemoteIdMacAddressState.setStatus(_A)
_ZyDhcpOption82ProfileRemoteIdString_Type=DisplayString
_ZyDhcpOption82ProfileRemoteIdString_Object=MibTableColumn
zyDhcpOption82ProfileRemoteIdString=_ZyDhcpOption82ProfileRemoteIdString_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,9),_ZyDhcpOption82ProfileRemoteIdString_Type())
zyDhcpOption82ProfileRemoteIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileRemoteIdString.setStatus(_A)
_ZyDhcpOption82ProfileRowstatus_Type=RowStatus
_ZyDhcpOption82ProfileRowstatus_Object=MibTableColumn
zyDhcpOption82ProfileRowstatus=_ZyDhcpOption82ProfileRowstatus_Object((1,3,6,1,4,1,890,1,15,3,17,1,2,1,10),_ZyDhcpOption82ProfileRowstatus_Type())
zyDhcpOption82ProfileRowstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpOption82ProfileRowstatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelDhcpOption82Profile':zyxelDhcpOption82Profile,'zyxelDhcpOption82ProfileSetup':zyxelDhcpOption82ProfileSetup,'zyDhcpOption82ProfileMaxNumberOfProfiles':zyDhcpOption82ProfileMaxNumberOfProfiles,'zyxelDhcpOption82ProfileTable':zyxelDhcpOption82ProfileTable,'zyxelDhcpOption82ProfileEntry':zyxelDhcpOption82ProfileEntry,_D:zyDhcpOption82ProfileName,'zyDhcpOption82ProfileCircuitIdState':zyDhcpOption82ProfileCircuitIdState,'zyDhcpOption82ProfileCircuitIdSlotPortState':zyDhcpOption82ProfileCircuitIdSlotPortState,'zyDhcpOption82ProfileCircuitIdVidState':zyDhcpOption82ProfileCircuitIdVidState,'zyDhcpOption82ProfileCircuitIdHostnameState':zyDhcpOption82ProfileCircuitIdHostnameState,'zyDhcpOption82ProfileCircuitIdString':zyDhcpOption82ProfileCircuitIdString,'zyDhcpOption82ProfileRemoteIdState':zyDhcpOption82ProfileRemoteIdState,'zyDhcpOption82ProfileRemoteIdMacAddressState':zyDhcpOption82ProfileRemoteIdMacAddressState,'zyDhcpOption82ProfileRemoteIdString':zyDhcpOption82ProfileRemoteIdString,'zyDhcpOption82ProfileRowstatus':zyDhcpOption82ProfileRowstatus})