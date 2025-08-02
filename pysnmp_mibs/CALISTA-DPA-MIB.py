_I='cmConnectionIndex'
_H='registering'
_G='DisplayString'
_F='notApplicable'
_E='portIndex'
_D='CALISTA-DPA-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Calista_ObjectIdentity=ObjectIdentity
calista=_Calista_ObjectIdentity((1,3,6,1,4,1,7505))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,7505,1))
_Dpa_ObjectIdentity=ObjectIdentity
dpa=_Dpa_ObjectIdentity((1,3,6,1,4,1,7505,1,1))
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,7505,1,1,1),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_ImageVersion_Type=DisplayString
_ImageVersion_Object=MibScalar
imageVersion=_ImageVersion_Object((1,3,6,1,4,1,7505,1,1,2),_ImageVersion_Type())
imageVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:imageVersion.setStatus(_A)
_LoaderVersion_Type=DisplayString
_LoaderVersion_Object=MibScalar
loaderVersion=_LoaderVersion_Object((1,3,6,1,4,1,7505,1,1,3),_LoaderVersion_Type())
loaderVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:loaderVersion.setStatus(_A)
class _IntegrationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unconfigured',1),('simple',2),('hybrid',3)))
_IntegrationMode_Type.__name__=_C
_IntegrationMode_Object=MibScalar
integrationMode=_IntegrationMode_Object((1,3,6,1,4,1,7505,1,1,4),_IntegrationMode_Type())
integrationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:integrationMode.setStatus(_A)
_PbxType_Type=DisplayString
_PbxType_Object=MibScalar
pbxType=_PbxType_Object((1,3,6,1,4,1,7505,1,1,5),_PbxType_Type())
pbxType.setMaxAccess(_B)
if mibBuilder.loadTexts:pbxType.setStatus(_A)
_ReceivedCalls_Type=Counter32
_ReceivedCalls_Object=MibScalar
receivedCalls=_ReceivedCalls_Object((1,3,6,1,4,1,7505,1,1,6),_ReceivedCalls_Type())
receivedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCalls.setStatus(_A)
_OutgoingCallsMade_Type=Counter32
_OutgoingCallsMade_Object=MibScalar
outgoingCallsMade=_OutgoingCallsMade_Object((1,3,6,1,4,1,7505,1,1,7),_OutgoingCallsMade_Type())
outgoingCallsMade.setMaxAccess(_B)
if mibBuilder.loadTexts:outgoingCallsMade.setStatus(_A)
_MwiCommandsReceived_Type=Counter32
_MwiCommandsReceived_Object=MibScalar
mwiCommandsReceived=_MwiCommandsReceived_Object((1,3,6,1,4,1,7505,1,1,8),_MwiCommandsReceived_Type())
mwiCommandsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:mwiCommandsReceived.setStatus(_A)
_PbxQueuedMWICommands_Type=Counter32
_PbxQueuedMWICommands_Object=MibScalar
pbxQueuedMWICommands=_PbxQueuedMWICommands_Object((1,3,6,1,4,1,7505,1,1,9),_PbxQueuedMWICommands_Type())
pbxQueuedMWICommands.setMaxAccess(_B)
if mibBuilder.loadTexts:pbxQueuedMWICommands.setStatus(_A)
_PbxCompletedMWICommands_Type=Counter32
_PbxCompletedMWICommands_Object=MibScalar
pbxCompletedMWICommands=_PbxCompletedMWICommands_Object((1,3,6,1,4,1,7505,1,1,10),_PbxCompletedMWICommands_Type())
pbxCompletedMWICommands.setMaxAccess(_B)
if mibBuilder.loadTexts:pbxCompletedMWICommands.setStatus(_A)
_PbxMWIErrors_Type=Counter32
_PbxMWIErrors_Object=MibScalar
pbxMWIErrors=_PbxMWIErrors_Object((1,3,6,1,4,1,7505,1,1,11),_PbxMWIErrors_Type())
pbxMWIErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pbxMWIErrors.setStatus(_A)
_CallManagerQueuedMWICommands_Type=Counter32
_CallManagerQueuedMWICommands_Object=MibScalar
callManagerQueuedMWICommands=_CallManagerQueuedMWICommands_Object((1,3,6,1,4,1,7505,1,1,12),_CallManagerQueuedMWICommands_Type())
callManagerQueuedMWICommands.setMaxAccess(_B)
if mibBuilder.loadTexts:callManagerQueuedMWICommands.setStatus(_A)
_CallManagerCompletedMWICommands_Type=Counter32
_CallManagerCompletedMWICommands_Object=MibScalar
callManagerCompletedMWICommands=_CallManagerCompletedMWICommands_Object((1,3,6,1,4,1,7505,1,1,13),_CallManagerCompletedMWICommands_Type())
callManagerCompletedMWICommands.setMaxAccess(_B)
if mibBuilder.loadTexts:callManagerCompletedMWICommands.setStatus(_A)
_CallManagerMWIErrors_Type=Counter32
_CallManagerMWIErrors_Object=MibScalar
callManagerMWIErrors=_CallManagerMWIErrors_Object((1,3,6,1,4,1,7505,1,1,14),_CallManagerMWIErrors_Type())
callManagerMWIErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:callManagerMWIErrors.setStatus(_A)
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,7505,1,1,15))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,7505,1,1,15,1))
portEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,7505,1,1,15,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notInUse',1),('octel',2),('pbx',3),('virtual',4)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,7505,1,1,15,1,2),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortTelephonyLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('down',2),(_H,3),('up',4)))
_PortTelephonyLinkState_Type.__name__=_C
_PortTelephonyLinkState_Object=MibTableColumn
portTelephonyLinkState=_PortTelephonyLinkState_Object((1,3,6,1,4,1,7505,1,1,15,1,3),_PortTelephonyLinkState_Type())
portTelephonyLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:portTelephonyLinkState.setStatus(_A)
class _PortCallManagerLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('down',2),(_H,3),('up',4)))
_PortCallManagerLinkState_Type.__name__=_C
_PortCallManagerLinkState_Object=MibTableColumn
portCallManagerLinkState=_PortCallManagerLinkState_Object((1,3,6,1,4,1,7505,1,1,15,1,4),_PortCallManagerLinkState_Type())
portCallManagerLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:portCallManagerLinkState.setStatus(_A)
class _PortCallState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknown',1),(_F,2),('onHook',3),('callIn',4),('callOut',5),('onCall',6),('offHook',7),('transfer',8),('outCall',9),('hangingUp',10)))
_PortCallState_Type.__name__=_C
_PortCallState_Object=MibTableColumn
portCallState=_PortCallState_Object((1,3,6,1,4,1,7505,1,1,15,1,5),_PortCallState_Type())
portCallState.setMaxAccess(_B)
if mibBuilder.loadTexts:portCallState.setStatus(_A)
_PortDeviceName_Type=DisplayString
_PortDeviceName_Object=MibTableColumn
portDeviceName=_PortDeviceName_Object((1,3,6,1,4,1,7505,1,1,15,1,6),_PortDeviceName_Type())
portDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:portDeviceName.setStatus(_A)
class _PortCodecInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('g711ALaw',2),('g711MuLaw',3),('g723dot1',4),('g729a',5)))
_PortCodecInUse_Type.__name__=_C
_PortCodecInUse_Object=MibTableColumn
portCodecInUse=_PortCodecInUse_Object((1,3,6,1,4,1,7505,1,1,15,1,7),_PortCodecInUse_Type())
portCodecInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:portCodecInUse.setStatus(_A)
_PortErrors_Type=Integer32
_PortErrors_Object=MibTableColumn
portErrors=_PortErrors_Object((1,3,6,1,4,1,7505,1,1,15,1,8),_PortErrors_Type())
portErrors.setMaxAccess('read-write')
if mibBuilder.loadTexts:portErrors.setStatus(_A)
_PortDacLevel_Type=Integer32
_PortDacLevel_Object=MibTableColumn
portDacLevel=_PortDacLevel_Object((1,3,6,1,4,1,7505,1,1,15,1,9),_PortDacLevel_Type())
portDacLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:portDacLevel.setStatus(_A)
_CallManagerConnectionTable_Object=MibTable
callManagerConnectionTable=_CallManagerConnectionTable_Object((1,3,6,1,4,1,7505,1,1,16))
if mibBuilder.loadTexts:callManagerConnectionTable.setStatus(_A)
_CallManagerConnectionEntry_Object=MibTableRow
callManagerConnectionEntry=_CallManagerConnectionEntry_Object((1,3,6,1,4,1,7505,1,1,16,1))
callManagerConnectionEntry.setIndexNames((0,_D,_E),(0,_D,_I))
if mibBuilder.loadTexts:callManagerConnectionEntry.setStatus(_A)
_CmConnectionPortIndex_Type=Integer32
_CmConnectionPortIndex_Object=MibTableColumn
cmConnectionPortIndex=_CmConnectionPortIndex_Object((1,3,6,1,4,1,7505,1,1,16,1,1),_CmConnectionPortIndex_Type())
cmConnectionPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionPortIndex.setStatus(_A)
_CmConnectionIndex_Type=Integer32
_CmConnectionIndex_Object=MibTableColumn
cmConnectionIndex=_CmConnectionIndex_Object((1,3,6,1,4,1,7505,1,1,16,1,2),_CmConnectionIndex_Type())
cmConnectionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionIndex.setStatus(_A)
_CmConnectionCallManagerName_Type=DisplayString
_CmConnectionCallManagerName_Object=MibTableColumn
cmConnectionCallManagerName=_CmConnectionCallManagerName_Object((1,3,6,1,4,1,7505,1,1,16,1,3),_CmConnectionCallManagerName_Type())
cmConnectionCallManagerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionCallManagerName.setStatus(_A)
_CmConnectionIpAddress_Type=IpAddress
_CmConnectionIpAddress_Object=MibTableColumn
cmConnectionIpAddress=_CmConnectionIpAddress_Object((1,3,6,1,4,1,7505,1,1,16,1,4),_CmConnectionIpAddress_Type())
cmConnectionIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionIpAddress.setStatus(_A)
class _CmConnectionIpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CmConnectionIpPort_Type.__name__=_C
_CmConnectionIpPort_Object=MibTableColumn
cmConnectionIpPort=_CmConnectionIpPort_Object((1,3,6,1,4,1,7505,1,1,16,1,5),_CmConnectionIpPort_Type())
cmConnectionIpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionIpPort.setStatus(_A)
class _CmConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connecting',2),('retryBackOff',3),('connectPending',4),('active',5),('standby',6)))
_CmConnectionState_Type.__name__=_C
_CmConnectionState_Object=MibTableColumn
cmConnectionState=_CmConnectionState_Object((1,3,6,1,4,1,7505,1,1,16,1,6),_CmConnectionState_Type())
cmConnectionState.setMaxAccess(_B)
if mibBuilder.loadTexts:cmConnectionState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_G:DisplayString,'calista':calista,'products':products,'dpa':dpa,'serialNumber':serialNumber,'imageVersion':imageVersion,'loaderVersion':loaderVersion,'integrationMode':integrationMode,'pbxType':pbxType,'receivedCalls':receivedCalls,'outgoingCallsMade':outgoingCallsMade,'mwiCommandsReceived':mwiCommandsReceived,'pbxQueuedMWICommands':pbxQueuedMWICommands,'pbxCompletedMWICommands':pbxCompletedMWICommands,'pbxMWIErrors':pbxMWIErrors,'callManagerQueuedMWICommands':callManagerQueuedMWICommands,'callManagerCompletedMWICommands':callManagerCompletedMWICommands,'callManagerMWIErrors':callManagerMWIErrors,'portTable':portTable,'portEntry':portEntry,_E:portIndex,'portType':portType,'portTelephonyLinkState':portTelephonyLinkState,'portCallManagerLinkState':portCallManagerLinkState,'portCallState':portCallState,'portDeviceName':portDeviceName,'portCodecInUse':portCodecInUse,'portErrors':portErrors,'portDacLevel':portDacLevel,'callManagerConnectionTable':callManagerConnectionTable,'callManagerConnectionEntry':callManagerConnectionEntry,'cmConnectionPortIndex':cmConnectionPortIndex,_I:cmConnectionIndex,'cmConnectionCallManagerName':cmConnectionCallManagerName,'cmConnectionIpAddress':cmConnectionIpAddress,'cmConnectionIpPort':cmConnectionIpPort,'cmConnectionState':cmConnectionState})