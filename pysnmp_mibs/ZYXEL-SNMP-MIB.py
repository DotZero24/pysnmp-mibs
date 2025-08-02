_K='zySnmpUserName'
_J='not-accessible'
_I='dot1dBasePort'
_H='BRIDGE-MIB'
_G='zySnmpTrapDestinationIpAddress'
_F='ZYXEL-SNMP-MIB'
_E='read-only'
_D='Integer32'
_C='Bits'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_H,_I)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSnmp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,76))
_ZyxelSnmpSetup_ObjectIdentity=ObjectIdentity
zyxelSnmpSetup=_ZyxelSnmpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,76,1))
_ZySnmpGetCommunity_Type=DisplayString
_ZySnmpGetCommunity_Object=MibScalar
zySnmpGetCommunity=_ZySnmpGetCommunity_Object((1,3,6,1,4,1,890,1,15,3,76,1,1),_ZySnmpGetCommunity_Type())
zySnmpGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpGetCommunity.setStatus(_A)
_ZySnmpSetCommunity_Type=DisplayString
_ZySnmpSetCommunity_Object=MibScalar
zySnmpSetCommunity=_ZySnmpSetCommunity_Object((1,3,6,1,4,1,890,1,15,3,76,1,2),_ZySnmpSetCommunity_Type())
zySnmpSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpSetCommunity.setStatus(_A)
_ZySnmpTrapCommunity_Type=DisplayString
_ZySnmpTrapCommunity_Object=MibScalar
zySnmpTrapCommunity=_ZySnmpTrapCommunity_Object((1,3,6,1,4,1,890,1,15,3,76,1,3),_ZySnmpTrapCommunity_Type())
zySnmpTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapCommunity.setStatus(_A)
_ZySnmpTrapDestinationMaxNumberOfDestinations_Type=Integer32
_ZySnmpTrapDestinationMaxNumberOfDestinations_Object=MibScalar
zySnmpTrapDestinationMaxNumberOfDestinations=_ZySnmpTrapDestinationMaxNumberOfDestinations_Object((1,3,6,1,4,1,890,1,15,3,76,1,4),_ZySnmpTrapDestinationMaxNumberOfDestinations_Type())
zySnmpTrapDestinationMaxNumberOfDestinations.setMaxAccess(_E)
if mibBuilder.loadTexts:zySnmpTrapDestinationMaxNumberOfDestinations.setStatus(_A)
_ZyxelSnmpTrapDestinationTable_Object=MibTable
zyxelSnmpTrapDestinationTable=_ZyxelSnmpTrapDestinationTable_Object((1,3,6,1,4,1,890,1,15,3,76,1,5))
if mibBuilder.loadTexts:zyxelSnmpTrapDestinationTable.setStatus(_A)
_ZyxelSnmpTrapDestinationEntry_Object=MibTableRow
zyxelSnmpTrapDestinationEntry=_ZyxelSnmpTrapDestinationEntry_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1))
zyxelSnmpTrapDestinationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelSnmpTrapDestinationEntry.setStatus(_A)
_ZySnmpTrapDestinationIpAddress_Type=IpAddress
_ZySnmpTrapDestinationIpAddress_Object=MibTableColumn
zySnmpTrapDestinationIpAddress=_ZySnmpTrapDestinationIpAddress_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1,1),_ZySnmpTrapDestinationIpAddress_Type())
zySnmpTrapDestinationIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:zySnmpTrapDestinationIpAddress.setStatus(_A)
_ZySnmpTrapDestinationUdpPort_Type=Integer32
_ZySnmpTrapDestinationUdpPort_Object=MibTableColumn
zySnmpTrapDestinationUdpPort=_ZySnmpTrapDestinationUdpPort_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1,2),_ZySnmpTrapDestinationUdpPort_Type())
zySnmpTrapDestinationUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapDestinationUdpPort.setStatus(_A)
class _ZySnmpTrapDestinationVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v1',0),('v2c',1),('v3',2)))
_ZySnmpTrapDestinationVersion_Type.__name__=_D
_ZySnmpTrapDestinationVersion_Object=MibTableColumn
zySnmpTrapDestinationVersion=_ZySnmpTrapDestinationVersion_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1,3),_ZySnmpTrapDestinationVersion_Type())
zySnmpTrapDestinationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapDestinationVersion.setStatus(_A)
_ZySnmpTrapDestinationUserName_Type=DisplayString
_ZySnmpTrapDestinationUserName_Object=MibTableColumn
zySnmpTrapDestinationUserName=_ZySnmpTrapDestinationUserName_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1,4),_ZySnmpTrapDestinationUserName_Type())
zySnmpTrapDestinationUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapDestinationUserName.setStatus(_A)
_ZySnmpTrapDestinationRowStatus_Type=RowStatus
_ZySnmpTrapDestinationRowStatus_Object=MibTableColumn
zySnmpTrapDestinationRowStatus=_ZySnmpTrapDestinationRowStatus_Object((1,3,6,1,4,1,890,1,15,3,76,1,5,1,5),_ZySnmpTrapDestinationRowStatus_Type())
zySnmpTrapDestinationRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zySnmpTrapDestinationRowStatus.setStatus(_A)
class _ZySnmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v2c',0),('v3',1),('v3v2c',2)))
_ZySnmpVersion_Type.__name__=_D
_ZySnmpVersion_Object=MibScalar
zySnmpVersion=_ZySnmpVersion_Object((1,3,6,1,4,1,890,1,15,3,76,1,6),_ZySnmpVersion_Type())
zySnmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpVersion.setStatus(_A)
_ZyxelSnmpUserTable_Object=MibTable
zyxelSnmpUserTable=_ZyxelSnmpUserTable_Object((1,3,6,1,4,1,890,1,15,3,76,1,7))
if mibBuilder.loadTexts:zyxelSnmpUserTable.setStatus(_A)
_ZyxelSnmpUserEntry_Object=MibTableRow
zyxelSnmpUserEntry=_ZyxelSnmpUserEntry_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1))
zyxelSnmpUserEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:zyxelSnmpUserEntry.setStatus(_A)
_ZySnmpUserName_Type=DisplayString
_ZySnmpUserName_Object=MibTableColumn
zySnmpUserName=_ZySnmpUserName_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1,1),_ZySnmpUserName_Type())
zySnmpUserName.setMaxAccess(_J)
if mibBuilder.loadTexts:zySnmpUserName.setStatus(_A)
class _ZySnmpUserSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAuthNoPriv',0),('authNoPriv',1),('authPriv',2)))
_ZySnmpUserSecurityLevel_Type.__name__=_D
_ZySnmpUserSecurityLevel_Object=MibTableColumn
zySnmpUserSecurityLevel=_ZySnmpUserSecurityLevel_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1,2),_ZySnmpUserSecurityLevel_Type())
zySnmpUserSecurityLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:zySnmpUserSecurityLevel.setStatus(_A)
class _ZySnmpUserAuthenticationProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('md5',0),('sha',1)))
_ZySnmpUserAuthenticationProtocol_Type.__name__=_D
_ZySnmpUserAuthenticationProtocol_Object=MibTableColumn
zySnmpUserAuthenticationProtocol=_ZySnmpUserAuthenticationProtocol_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1,3),_ZySnmpUserAuthenticationProtocol_Type())
zySnmpUserAuthenticationProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:zySnmpUserAuthenticationProtocol.setStatus(_A)
class _ZySnmpUserPrivacyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('des',0),('aes',1)))
_ZySnmpUserPrivacyProtocol_Type.__name__=_D
_ZySnmpUserPrivacyProtocol_Object=MibTableColumn
zySnmpUserPrivacyProtocol=_ZySnmpUserPrivacyProtocol_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1,4),_ZySnmpUserPrivacyProtocol_Type())
zySnmpUserPrivacyProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:zySnmpUserPrivacyProtocol.setStatus(_A)
_ZySnmpUserGroup_Type=DisplayString
_ZySnmpUserGroup_Object=MibTableColumn
zySnmpUserGroup=_ZySnmpUserGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,7,1,5),_ZySnmpUserGroup_Type())
zySnmpUserGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:zySnmpUserGroup.setStatus(_A)
_ZyxelSnmpTrapGroupTable_Object=MibTable
zyxelSnmpTrapGroupTable=_ZyxelSnmpTrapGroupTable_Object((1,3,6,1,4,1,890,1,15,3,76,1,8))
if mibBuilder.loadTexts:zyxelSnmpTrapGroupTable.setStatus(_A)
_ZyxelSnmpTrapGroupEntry_Object=MibTableRow
zyxelSnmpTrapGroupEntry=_ZyxelSnmpTrapGroupEntry_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1))
zyxelSnmpTrapGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelSnmpTrapGroupEntry.setStatus(_A)
class _ZySnmpTrapSysGroup_Type(Bits):namedValues=NamedValues(*(('coldStart',0),('warmStart',1),('fanSpeed',2),('temperature',3),('voltage',4),('reset',5),('timeSync',6),('intrusionlock',7),('bps',8),('maintainence',9),('externalalarm',10),('powerportfailed',11),('errorlog',12),('loopGuard',13),('errdisable',14),('dyinggasp',15),('poe',16),('fanairflow',17),('stacking',18),('powerSource',19),('loginRecord',20)))
_ZySnmpTrapSysGroup_Type.__name__=_C
_ZySnmpTrapSysGroup_Object=MibTableColumn
zySnmpTrapSysGroup=_ZySnmpTrapSysGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1,1),_ZySnmpTrapSysGroup_Type())
zySnmpTrapSysGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapSysGroup.setStatus(_A)
class _ZySnmpTrapInterfaceGroup_Type(Bits):namedValues=NamedValues(*(('linkup',0),('linkdown',1),('autonegotiation',2),('lldp',3),('transceiverDdm',4),('module',5),('stormControl',6),('zuld',7)))
_ZySnmpTrapInterfaceGroup_Type.__name__=_C
_ZySnmpTrapInterfaceGroup_Object=MibTableColumn
zySnmpTrapInterfaceGroup=_ZySnmpTrapInterfaceGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1,2),_ZySnmpTrapInterfaceGroup_Type())
zySnmpTrapInterfaceGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapInterfaceGroup.setStatus(_A)
class _ZySnmpTrapAAAGroup_Type(Bits):namedValues=NamedValues(*(('authentication',0),('authorization',1),('accounting',2)))
_ZySnmpTrapAAAGroup_Type.__name__=_C
_ZySnmpTrapAAAGroup_Object=MibTableColumn
zySnmpTrapAAAGroup=_ZySnmpTrapAAAGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1,3),_ZySnmpTrapAAAGroup_Type())
zySnmpTrapAAAGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapAAAGroup.setStatus(_A)
class _ZySnmpTrapIPGroup_Type(Bits):namedValues=NamedValues(*(('ping',0),('traceroute',1)))
_ZySnmpTrapIPGroup_Type.__name__=_C
_ZySnmpTrapIPGroup_Object=MibTableColumn
zySnmpTrapIPGroup=_ZySnmpTrapIPGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1,4),_ZySnmpTrapIPGroup_Type())
zySnmpTrapIPGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapIPGroup.setStatus(_A)
class _ZySnmpTrapSwitchGroup_Type(Bits):namedValues=NamedValues(*(('stp',0),('mactable',1),('rmon',2),('cfm',3),('classifier',4),('rip',5),('ospf',6)))
_ZySnmpTrapSwitchGroup_Type.__name__=_C
_ZySnmpTrapSwitchGroup_Object=MibTableColumn
zySnmpTrapSwitchGroup=_ZySnmpTrapSwitchGroup_Object((1,3,6,1,4,1,890,1,15,3,76,1,8,1,5),_ZySnmpTrapSwitchGroup_Type())
zySnmpTrapSwitchGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapSwitchGroup.setStatus(_A)
_ZyxelSnmpTrapPortTable_Object=MibTable
zyxelSnmpTrapPortTable=_ZyxelSnmpTrapPortTable_Object((1,3,6,1,4,1,890,1,15,3,76,1,9))
if mibBuilder.loadTexts:zyxelSnmpTrapPortTable.setStatus(_A)
_ZyxelSnmpTrapPortEntry_Object=MibTableRow
zyxelSnmpTrapPortEntry=_ZyxelSnmpTrapPortEntry_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1))
zyxelSnmpTrapPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zyxelSnmpTrapPortEntry.setStatus(_A)
_ZySnmpTrapPortIntrusionlockState_Type=EnabledStatus
_ZySnmpTrapPortIntrusionlockState_Object=MibTableColumn
zySnmpTrapPortIntrusionlockState=_ZySnmpTrapPortIntrusionlockState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,1),_ZySnmpTrapPortIntrusionlockState_Type())
zySnmpTrapPortIntrusionlockState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortIntrusionlockState.setStatus(_A)
_ZySnmpTrapPortLoopguardState_Type=EnabledStatus
_ZySnmpTrapPortLoopguardState_Object=MibTableColumn
zySnmpTrapPortLoopguardState=_ZySnmpTrapPortLoopguardState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,2),_ZySnmpTrapPortLoopguardState_Type())
zySnmpTrapPortLoopguardState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortLoopguardState.setStatus(_A)
_ZySnmpTrapPortErrdisableState_Type=EnabledStatus
_ZySnmpTrapPortErrdisableState_Object=MibTableColumn
zySnmpTrapPortErrdisableState=_ZySnmpTrapPortErrdisableState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,3),_ZySnmpTrapPortErrdisableState_Type())
zySnmpTrapPortErrdisableState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortErrdisableState.setStatus(_A)
_ZySnmpTrapPortPoeState_Type=EnabledStatus
_ZySnmpTrapPortPoeState_Object=MibTableColumn
zySnmpTrapPortPoeState=_ZySnmpTrapPortPoeState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,4),_ZySnmpTrapPortPoeState_Type())
zySnmpTrapPortPoeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortPoeState.setStatus(_A)
_ZySnmpTrapPortLinkupState_Type=EnabledStatus
_ZySnmpTrapPortLinkupState_Object=MibTableColumn
zySnmpTrapPortLinkupState=_ZySnmpTrapPortLinkupState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,5),_ZySnmpTrapPortLinkupState_Type())
zySnmpTrapPortLinkupState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortLinkupState.setStatus(_A)
_ZySnmpTrapPortLinkdownState_Type=EnabledStatus
_ZySnmpTrapPortLinkdownState_Object=MibTableColumn
zySnmpTrapPortLinkdownState=_ZySnmpTrapPortLinkdownState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,6),_ZySnmpTrapPortLinkdownState_Type())
zySnmpTrapPortLinkdownState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortLinkdownState.setStatus(_A)
_ZySnmpTrapPortAutonegotiationState_Type=EnabledStatus
_ZySnmpTrapPortAutonegotiationState_Object=MibTableColumn
zySnmpTrapPortAutonegotiationState=_ZySnmpTrapPortAutonegotiationState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,7),_ZySnmpTrapPortAutonegotiationState_Type())
zySnmpTrapPortAutonegotiationState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortAutonegotiationState.setStatus(_A)
_ZySnmpTrapPortLldpState_Type=EnabledStatus
_ZySnmpTrapPortLldpState_Object=MibTableColumn
zySnmpTrapPortLldpState=_ZySnmpTrapPortLldpState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,8),_ZySnmpTrapPortLldpState_Type())
zySnmpTrapPortLldpState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortLldpState.setStatus(_A)
_ZySnmpTrapPortTransceiverDdmState_Type=EnabledStatus
_ZySnmpTrapPortTransceiverDdmState_Object=MibTableColumn
zySnmpTrapPortTransceiverDdmState=_ZySnmpTrapPortTransceiverDdmState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,9),_ZySnmpTrapPortTransceiverDdmState_Type())
zySnmpTrapPortTransceiverDdmState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortTransceiverDdmState.setStatus(_A)
_ZySnmpTrapPortStormControlState_Type=EnabledStatus
_ZySnmpTrapPortStormControlState_Object=MibTableColumn
zySnmpTrapPortStormControlState=_ZySnmpTrapPortStormControlState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,10),_ZySnmpTrapPortStormControlState_Type())
zySnmpTrapPortStormControlState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortStormControlState.setStatus(_A)
_ZySnmpTrapPortZuldState_Type=EnabledStatus
_ZySnmpTrapPortZuldState_Object=MibTableColumn
zySnmpTrapPortZuldState=_ZySnmpTrapPortZuldState_Object((1,3,6,1,4,1,890,1,15,3,76,1,9,1,11),_ZySnmpTrapPortZuldState_Type())
zySnmpTrapPortZuldState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySnmpTrapPortZuldState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zyxelSnmp':zyxelSnmp,'zyxelSnmpSetup':zyxelSnmpSetup,'zySnmpGetCommunity':zySnmpGetCommunity,'zySnmpSetCommunity':zySnmpSetCommunity,'zySnmpTrapCommunity':zySnmpTrapCommunity,'zySnmpTrapDestinationMaxNumberOfDestinations':zySnmpTrapDestinationMaxNumberOfDestinations,'zyxelSnmpTrapDestinationTable':zyxelSnmpTrapDestinationTable,'zyxelSnmpTrapDestinationEntry':zyxelSnmpTrapDestinationEntry,_G:zySnmpTrapDestinationIpAddress,'zySnmpTrapDestinationUdpPort':zySnmpTrapDestinationUdpPort,'zySnmpTrapDestinationVersion':zySnmpTrapDestinationVersion,'zySnmpTrapDestinationUserName':zySnmpTrapDestinationUserName,'zySnmpTrapDestinationRowStatus':zySnmpTrapDestinationRowStatus,'zySnmpVersion':zySnmpVersion,'zyxelSnmpUserTable':zyxelSnmpUserTable,'zyxelSnmpUserEntry':zyxelSnmpUserEntry,_K:zySnmpUserName,'zySnmpUserSecurityLevel':zySnmpUserSecurityLevel,'zySnmpUserAuthenticationProtocol':zySnmpUserAuthenticationProtocol,'zySnmpUserPrivacyProtocol':zySnmpUserPrivacyProtocol,'zySnmpUserGroup':zySnmpUserGroup,'zyxelSnmpTrapGroupTable':zyxelSnmpTrapGroupTable,'zyxelSnmpTrapGroupEntry':zyxelSnmpTrapGroupEntry,'zySnmpTrapSysGroup':zySnmpTrapSysGroup,'zySnmpTrapInterfaceGroup':zySnmpTrapInterfaceGroup,'zySnmpTrapAAAGroup':zySnmpTrapAAAGroup,'zySnmpTrapIPGroup':zySnmpTrapIPGroup,'zySnmpTrapSwitchGroup':zySnmpTrapSwitchGroup,'zyxelSnmpTrapPortTable':zyxelSnmpTrapPortTable,'zyxelSnmpTrapPortEntry':zyxelSnmpTrapPortEntry,'zySnmpTrapPortIntrusionlockState':zySnmpTrapPortIntrusionlockState,'zySnmpTrapPortLoopguardState':zySnmpTrapPortLoopguardState,'zySnmpTrapPortErrdisableState':zySnmpTrapPortErrdisableState,'zySnmpTrapPortPoeState':zySnmpTrapPortPoeState,'zySnmpTrapPortLinkupState':zySnmpTrapPortLinkupState,'zySnmpTrapPortLinkdownState':zySnmpTrapPortLinkdownState,'zySnmpTrapPortAutonegotiationState':zySnmpTrapPortAutonegotiationState,'zySnmpTrapPortLldpState':zySnmpTrapPortLldpState,'zySnmpTrapPortTransceiverDdmState':zySnmpTrapPortTransceiverDdmState,'zySnmpTrapPortStormControlState':zySnmpTrapPortStormControlState,'zySnmpTrapPortZuldState':zySnmpTrapPortZuldState})