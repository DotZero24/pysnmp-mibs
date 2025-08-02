_s='cCallHistoryIecGroup'
_r='cCallHistoryGroupRev1'
_q='cCallHistoryGroup'
_p='cCallHistoryIec'
_o='cPeerSearchType'
_n='cCallHistoryReleaseSrc'
_m='cCallHistoryReleaseSource'
_l='cCallHistoryIecIndex'
_k='externalCallControlAgent'
_j='externalNmsApp'
_i='externalRadiusServer'
_h='consoleCommand'
_g='internalCallControlApp'
_f='calledPartyInVoip'
_e='calledPartyInPstn'
_d='callingPartyInVoip'
_c='callingPartyInPstn'
_b='not-accessible'
_a='OctetString'
_Z='cPeerGlobalConfigurationGroup'
_Y='cCallHistoryIndex'
_X='Unsigned32'
_W='cCallHistoryGroupRev2'
_V='cCallHistoryReceiveBytes'
_U='cCallHistoryReceivePackets'
_T='cCallHistoryTransmitBytes'
_S='cCallHistoryTransmitPackets'
_R='cCallHistoryInfoType'
_Q='cCallHistoryChargedUnits'
_P='cCallHistoryCallOrigin'
_O='cCallHistoryDisconnectTime'
_N='cCallHistoryConnectTime'
_M='cCallHistoryDisconnectText'
_L='cCallHistoryDisconnectCause'
_K='cCallHistoryLogicalIfIndex'
_J='cCallHistoryPeerIfIndex'
_I='cCallHistoryPeerId'
_H='cCallHistoryPeerSubAddress'
_G='cCallHistoryPeerAddress'
_F='cCallHistorySetupTime'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-DIAL-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
AbsoluteCounter32,=mibBuilder.importSymbols('DIAL-CONTROL-MIB','AbsoluteCounter32')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoDialControlMib=ModuleIdentity((1,3,6,1,4,1,9,10,25))
if mibBuilder.loadTexts:ciscoDialControlMib.setRevisions(('2005-05-26 00:00','2003-07-10 00:01','2002-08-21 00:01','2002-05-24 00:01','2002-02-20 15:46','2001-12-13 15:46','1998-01-16 15:46'))
_CiscoDialControlMibObjects_ObjectIdentity=ObjectIdentity
ciscoDialControlMibObjects=_CiscoDialControlMibObjects_ObjectIdentity((1,3,6,1,4,1,9,10,25,1))
_CCallHistory_ObjectIdentity=ObjectIdentity
cCallHistory=_CCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,25,1,4))
_CCallHistoryTable_Object=MibTable
cCallHistoryTable=_CCallHistoryTable_Object((1,3,6,1,4,1,9,10,25,1,4,3))
if mibBuilder.loadTexts:cCallHistoryTable.setStatus(_B)
_CCallHistoryEntry_Object=MibTableRow
cCallHistoryEntry=_CCallHistoryEntry_Object((1,3,6,1,4,1,9,10,25,1,4,3,1))
cCallHistoryEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:cCallHistoryEntry.setStatus(_B)
class _CCallHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CCallHistoryIndex_Type.__name__=_X
_CCallHistoryIndex_Object=MibTableColumn
cCallHistoryIndex=_CCallHistoryIndex_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,1),_CCallHistoryIndex_Type())
cCallHistoryIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:cCallHistoryIndex.setStatus(_B)
_CCallHistorySetupTime_Type=TimeStamp
_CCallHistorySetupTime_Object=MibTableColumn
cCallHistorySetupTime=_CCallHistorySetupTime_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,2),_CCallHistorySetupTime_Type())
cCallHistorySetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistorySetupTime.setStatus(_B)
_CCallHistoryPeerAddress_Type=DisplayString
_CCallHistoryPeerAddress_Object=MibTableColumn
cCallHistoryPeerAddress=_CCallHistoryPeerAddress_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,3),_CCallHistoryPeerAddress_Type())
cCallHistoryPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryPeerAddress.setStatus(_B)
_CCallHistoryPeerSubAddress_Type=DisplayString
_CCallHistoryPeerSubAddress_Object=MibTableColumn
cCallHistoryPeerSubAddress=_CCallHistoryPeerSubAddress_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,4),_CCallHistoryPeerSubAddress_Type())
cCallHistoryPeerSubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryPeerSubAddress.setStatus(_B)
class _CCallHistoryPeerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CCallHistoryPeerId_Type.__name__=_D
_CCallHistoryPeerId_Object=MibTableColumn
cCallHistoryPeerId=_CCallHistoryPeerId_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,5),_CCallHistoryPeerId_Type())
cCallHistoryPeerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryPeerId.setStatus(_B)
class _CCallHistoryPeerIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CCallHistoryPeerIfIndex_Type.__name__=_D
_CCallHistoryPeerIfIndex_Object=MibTableColumn
cCallHistoryPeerIfIndex=_CCallHistoryPeerIfIndex_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,6),_CCallHistoryPeerIfIndex_Type())
cCallHistoryPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryPeerIfIndex.setStatus(_B)
_CCallHistoryLogicalIfIndex_Type=InterfaceIndexOrZero
_CCallHistoryLogicalIfIndex_Object=MibTableColumn
cCallHistoryLogicalIfIndex=_CCallHistoryLogicalIfIndex_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,7),_CCallHistoryLogicalIfIndex_Type())
cCallHistoryLogicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryLogicalIfIndex.setStatus(_B)
class _CCallHistoryDisconnectCause_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CCallHistoryDisconnectCause_Type.__name__=_a
_CCallHistoryDisconnectCause_Object=MibTableColumn
cCallHistoryDisconnectCause=_CCallHistoryDisconnectCause_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,8),_CCallHistoryDisconnectCause_Type())
cCallHistoryDisconnectCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryDisconnectCause.setStatus(_B)
_CCallHistoryDisconnectText_Type=DisplayString
_CCallHistoryDisconnectText_Object=MibTableColumn
cCallHistoryDisconnectText=_CCallHistoryDisconnectText_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,9),_CCallHistoryDisconnectText_Type())
cCallHistoryDisconnectText.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryDisconnectText.setStatus(_B)
_CCallHistoryConnectTime_Type=TimeStamp
_CCallHistoryConnectTime_Object=MibTableColumn
cCallHistoryConnectTime=_CCallHistoryConnectTime_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,10),_CCallHistoryConnectTime_Type())
cCallHistoryConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryConnectTime.setStatus(_B)
_CCallHistoryDisconnectTime_Type=TimeStamp
_CCallHistoryDisconnectTime_Object=MibTableColumn
cCallHistoryDisconnectTime=_CCallHistoryDisconnectTime_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,11),_CCallHistoryDisconnectTime_Type())
cCallHistoryDisconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryDisconnectTime.setStatus(_B)
class _CCallHistoryCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('originate',1),('answer',2),('callback',3)))
_CCallHistoryCallOrigin_Type.__name__=_D
_CCallHistoryCallOrigin_Object=MibTableColumn
cCallHistoryCallOrigin=_CCallHistoryCallOrigin_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,12),_CCallHistoryCallOrigin_Type())
cCallHistoryCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryCallOrigin.setStatus(_B)
_CCallHistoryChargedUnits_Type=AbsoluteCounter32
_CCallHistoryChargedUnits_Object=MibTableColumn
cCallHistoryChargedUnits=_CCallHistoryChargedUnits_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,13),_CCallHistoryChargedUnits_Type())
cCallHistoryChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryChargedUnits.setStatus(_B)
class _CCallHistoryInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('speech',2),('unrestrictedDigital',3),('unrestrictedDigital56',4),('restrictedDigital',5),('audio31',6),('audio7',7),('video',8),('packetSwitched',9),('fax',10)))
_CCallHistoryInfoType_Type.__name__=_D
_CCallHistoryInfoType_Object=MibTableColumn
cCallHistoryInfoType=_CCallHistoryInfoType_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,14),_CCallHistoryInfoType_Type())
cCallHistoryInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryInfoType.setStatus(_B)
_CCallHistoryTransmitPackets_Type=AbsoluteCounter32
_CCallHistoryTransmitPackets_Object=MibTableColumn
cCallHistoryTransmitPackets=_CCallHistoryTransmitPackets_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,15),_CCallHistoryTransmitPackets_Type())
cCallHistoryTransmitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryTransmitPackets.setStatus(_B)
_CCallHistoryTransmitBytes_Type=AbsoluteCounter32
_CCallHistoryTransmitBytes_Object=MibTableColumn
cCallHistoryTransmitBytes=_CCallHistoryTransmitBytes_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,16),_CCallHistoryTransmitBytes_Type())
cCallHistoryTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryTransmitBytes.setStatus(_B)
_CCallHistoryReceivePackets_Type=AbsoluteCounter32
_CCallHistoryReceivePackets_Object=MibTableColumn
cCallHistoryReceivePackets=_CCallHistoryReceivePackets_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,17),_CCallHistoryReceivePackets_Type())
cCallHistoryReceivePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryReceivePackets.setStatus(_B)
_CCallHistoryReceiveBytes_Type=AbsoluteCounter32
_CCallHistoryReceiveBytes_Object=MibTableColumn
cCallHistoryReceiveBytes=_CCallHistoryReceiveBytes_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,18),_CCallHistoryReceiveBytes_Type())
cCallHistoryReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryReceiveBytes.setStatus(_B)
class _CCallHistoryReleaseSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),('internalRelease',5),(_g,6),(_h,7),(_i,8),(_j,9),(_k,10)))
_CCallHistoryReleaseSource_Type.__name__=_D
_CCallHistoryReleaseSource_Object=MibTableColumn
cCallHistoryReleaseSource=_CCallHistoryReleaseSource_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,19),_CCallHistoryReleaseSource_Type())
cCallHistoryReleaseSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryReleaseSource.setStatus(_E)
class _CCallHistoryReleaseSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),('internalReleaseInPotsLeg',5),('internalReleaseInVoipLeg',6),(_g,7),('internalReleaseInVoipAAA',8),(_h,9),(_i,10),(_j,11),(_k,12),('gatekeeper',13),('externalGKTMPServer',14)))
_CCallHistoryReleaseSrc_Type.__name__=_D
_CCallHistoryReleaseSrc_Object=MibTableColumn
cCallHistoryReleaseSrc=_CCallHistoryReleaseSrc_Object((1,3,6,1,4,1,9,10,25,1,4,3,1,20),_CCallHistoryReleaseSrc_Type())
cCallHistoryReleaseSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryReleaseSrc.setStatus(_B)
_CCallHistoryIecTable_Object=MibTable
cCallHistoryIecTable=_CCallHistoryIecTable_Object((1,3,6,1,4,1,9,10,25,1,4,4))
if mibBuilder.loadTexts:cCallHistoryIecTable.setStatus(_B)
_CCallHistoryIecEntry_Object=MibTableRow
cCallHistoryIecEntry=_CCallHistoryIecEntry_Object((1,3,6,1,4,1,9,10,25,1,4,4,1))
cCallHistoryIecEntry.setIndexNames((0,_A,_Y),(0,_A,_l))
if mibBuilder.loadTexts:cCallHistoryIecEntry.setStatus(_B)
class _CCallHistoryIecIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CCallHistoryIecIndex_Type.__name__=_X
_CCallHistoryIecIndex_Object=MibTableColumn
cCallHistoryIecIndex=_CCallHistoryIecIndex_Object((1,3,6,1,4,1,9,10,25,1,4,4,1,1),_CCallHistoryIecIndex_Type())
cCallHistoryIecIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:cCallHistoryIecIndex.setStatus(_B)
_CCallHistoryIec_Type=SnmpAdminString
_CCallHistoryIec_Object=MibTableColumn
cCallHistoryIec=_CCallHistoryIec_Object((1,3,6,1,4,1,9,10,25,1,4,4,1,2),_CCallHistoryIec_Type())
cCallHistoryIec.setMaxAccess(_C)
if mibBuilder.loadTexts:cCallHistoryIec.setStatus(_B)
_CPeerGlobalConfiguration_ObjectIdentity=ObjectIdentity
cPeerGlobalConfiguration=_CPeerGlobalConfiguration_ObjectIdentity((1,3,6,1,4,1,9,10,25,1,5))
class _CPeerSearchType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('datavoice',2),('voicedata',3)))
_CPeerSearchType_Type.__name__=_D
_CPeerSearchType_Object=MibScalar
cPeerSearchType=_CPeerSearchType_Object((1,3,6,1,4,1,9,10,25,1,5,1),_CPeerSearchType_Type())
cPeerSearchType.setMaxAccess('read-write')
if mibBuilder.loadTexts:cPeerSearchType.setStatus(_B)
_CiscoDialControlMibConformance_ObjectIdentity=ObjectIdentity
ciscoDialControlMibConformance=_CiscoDialControlMibConformance_ObjectIdentity((1,3,6,1,4,1,9,10,25,3))
_CiscoDialControlMibCompliances_ObjectIdentity=ObjectIdentity
ciscoDialControlMibCompliances=_CiscoDialControlMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,25,3,1))
_CiscoDialControlMibGroups_ObjectIdentity=ObjectIdentity
ciscoDialControlMibGroups=_CiscoDialControlMibGroups_ObjectIdentity((1,3,6,1,4,1,9,10,25,3,2))
cCallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,25,3,2,1))
cCallHistoryGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cCallHistoryGroup.setStatus(_E)
cCallHistoryGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,25,3,2,2))
cCallHistoryGroupRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_m)))
if mibBuilder.loadTexts:cCallHistoryGroupRev1.setStatus(_E)
cCallHistoryGroupRev2=ObjectGroup((1,3,6,1,4,1,9,10,25,3,2,3))
cCallHistoryGroupRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_n)))
if mibBuilder.loadTexts:cCallHistoryGroupRev2.setStatus(_B)
cPeerGlobalConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,10,25,3,2,4))
cPeerGlobalConfigurationGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:cPeerGlobalConfigurationGroup.setStatus(_B)
cCallHistoryIecGroup=ObjectGroup((1,3,6,1,4,1,9,10,25,3,2,5))
cCallHistoryIecGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:cCallHistoryIecGroup.setStatus(_B)
ciscoDialControlMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,25,3,1,1))
ciscoDialControlMibCompliance.setObjects((_A,_q))
if mibBuilder.loadTexts:ciscoDialControlMibCompliance.setStatus(_E)
ciscoDialControlMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,25,3,1,2))
ciscoDialControlMibComplianceRev1.setObjects((_A,_r))
if mibBuilder.loadTexts:ciscoDialControlMibComplianceRev1.setStatus(_E)
ciscoDialControlMibComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,10,25,3,1,3))
ciscoDialControlMibComplianceRev2.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoDialControlMibComplianceRev2.setStatus(_E)
ciscoDialControlMibComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,10,25,3,1,4))
ciscoDialControlMibComplianceRev3.setObjects(*((_A,_W),(_A,_Z)))
if mibBuilder.loadTexts:ciscoDialControlMibComplianceRev3.setStatus(_E)
ciscoDialControlMibComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,10,25,3,1,5))
ciscoDialControlMibComplianceRev4.setObjects(*((_A,_W),(_A,_Z),(_A,_s)))
if mibBuilder.loadTexts:ciscoDialControlMibComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDialControlMib':ciscoDialControlMib,'ciscoDialControlMibObjects':ciscoDialControlMibObjects,'cCallHistory':cCallHistory,'cCallHistoryTable':cCallHistoryTable,'cCallHistoryEntry':cCallHistoryEntry,_Y:cCallHistoryIndex,_F:cCallHistorySetupTime,_G:cCallHistoryPeerAddress,_H:cCallHistoryPeerSubAddress,_I:cCallHistoryPeerId,_J:cCallHistoryPeerIfIndex,_K:cCallHistoryLogicalIfIndex,_L:cCallHistoryDisconnectCause,_M:cCallHistoryDisconnectText,_N:cCallHistoryConnectTime,_O:cCallHistoryDisconnectTime,_P:cCallHistoryCallOrigin,_Q:cCallHistoryChargedUnits,_R:cCallHistoryInfoType,_S:cCallHistoryTransmitPackets,_T:cCallHistoryTransmitBytes,_U:cCallHistoryReceivePackets,_V:cCallHistoryReceiveBytes,_m:cCallHistoryReleaseSource,_n:cCallHistoryReleaseSrc,'cCallHistoryIecTable':cCallHistoryIecTable,'cCallHistoryIecEntry':cCallHistoryIecEntry,_l:cCallHistoryIecIndex,_p:cCallHistoryIec,'cPeerGlobalConfiguration':cPeerGlobalConfiguration,_o:cPeerSearchType,'ciscoDialControlMibConformance':ciscoDialControlMibConformance,'ciscoDialControlMibCompliances':ciscoDialControlMibCompliances,'ciscoDialControlMibCompliance':ciscoDialControlMibCompliance,'ciscoDialControlMibComplianceRev1':ciscoDialControlMibComplianceRev1,'ciscoDialControlMibComplianceRev2':ciscoDialControlMibComplianceRev2,'ciscoDialControlMibComplianceRev3':ciscoDialControlMibComplianceRev3,'ciscoDialControlMibComplianceRev4':ciscoDialControlMibComplianceRev4,'ciscoDialControlMibGroups':ciscoDialControlMibGroups,_q:cCallHistoryGroup,_r:cCallHistoryGroupRev1,_W:cCallHistoryGroupRev2,_Z:cPeerGlobalConfigurationGroup,_s:cCallHistoryIecGroup})