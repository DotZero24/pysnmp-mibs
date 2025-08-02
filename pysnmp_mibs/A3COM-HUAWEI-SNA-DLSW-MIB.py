_h='dlswCircuitS2Sap'
_g='dlswCircuitS2Mac'
_f='dlswCircuitS1Sap'
_e='dlswCircuitS1Mac'
_d='dlswCircuitState'
_c='dlswRemotePeerLinkState'
_b='dlswBridgeIfBriGru'
_a='dlswSdlcLsAddress'
_Z='hundredths of a second'
_Y='dlswLocMacHashIndexSeqNum'
_X='dlswLocMacHashIndex'
_W='dlswBridgeNum'
_V='disconnected'
_U='connected'
_T='accessible-for-notify'
_S='LFSize'
_R='disenable'
_Q='enable'
_P='dlswCircuitS1CircuitId'
_O='unknown'
_N='other'
_M='not-accessible'
_L='no'
_K='yes'
_J='dlswRemotePeerAddr'
_I='ifIndex'
_H='IF-MIB'
_G='OctetString'
_F='obsolete'
_E='A3COM-HUAWEI-SNA-DLSW-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwproducts,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','hwproducts')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlsw=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,34))
class MacAddressNC(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
class EndStationLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('internal',2),('remote',3),('local',4)))
class DlcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('na',2),('llc',3),('sdlc',4),('qllc',5)))
class LFSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(516,1470,1500,2052,4472,8144,11407,11454,17800,65535)));namedValues=NamedValues(*(('lfs516',516),('lfs1470',1470),('lfs1500',1500),('lfs2052',2052),('lfs4472',4472),('lfs8144',8144),('lfs11407',11407),('lfs11454',11454),('lfs17800',17800),(_O,65535)))
class CreateLineFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('createLine',1),('deleteLine',2)))
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_DlswNode_ObjectIdentity=ObjectIdentity
dlswNode=_DlswNode_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,1))
class _DlswNodeVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DlswNodeVersion_Type.__name__=_G
_DlswNodeVersion_Object=MibScalar
dlswNodeVersion=_DlswNodeVersion_Object((1,3,6,1,4,1,43,45,1,2,34,1,1),_DlswNodeVersion_Type())
dlswNodeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswNodeVersion.setStatus(_A)
class _DlswNodeVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_DlswNodeVendorID_Type.__name__=_G
_DlswNodeVendorID_Object=MibScalar
dlswNodeVendorID=_DlswNodeVendorID_Object((1,3,6,1,4,1,43,45,1,2,34,1,2),_DlswNodeVendorID_Type())
dlswNodeVendorID.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswNodeVendorID.setStatus(_A)
_DlswNodeVersionString_Type=DisplayString
_DlswNodeVersionString_Object=MibScalar
dlswNodeVersionString=_DlswNodeVersionString_Object((1,3,6,1,4,1,43,45,1,2,34,1,3),_DlswNodeVersionString_Type())
dlswNodeVersionString.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswNodeVersionString.setStatus(_A)
class _DlswNodeStdPacingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,65535)));namedValues=NamedValues(*(('none',1),('adaptiveRcvWindow',2),('fixedRcvWindow',3),(_O,65535)))
_DlswNodeStdPacingSupport_Type.__name__=_B
_DlswNodeStdPacingSupport_Object=MibScalar
dlswNodeStdPacingSupport=_DlswNodeStdPacingSupport_Object((1,3,6,1,4,1,43,45,1,2,34,1,4),_DlswNodeStdPacingSupport_Type())
dlswNodeStdPacingSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswNodeStdPacingSupport.setStatus(_A)
class _DlswNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_DlswNodeStatus_Type.__name__=_B
_DlswNodeStatus_Object=MibScalar
dlswNodeStatus=_DlswNodeStatus_Object((1,3,6,1,4,1,43,45,1,2,34,1,5),_DlswNodeStatus_Type())
dlswNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeStatus.setStatus(_A)
_DlswNodeUpTime_Type=Integer32
_DlswNodeUpTime_Object=MibScalar
dlswNodeUpTime=_DlswNodeUpTime_Object((1,3,6,1,4,1,43,45,1,2,34,1,6),_DlswNodeUpTime_Type())
dlswNodeUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswNodeUpTime.setStatus(_F)
if mibBuilder.loadTexts:dlswNodeUpTime.setUnits('second')
class _DlswNodeVirtualSegmentLFSize_Type(LFSize):defaultValue=1500
_DlswNodeVirtualSegmentLFSize_Type.__name__=_S
_DlswNodeVirtualSegmentLFSize_Object=MibScalar
dlswNodeVirtualSegmentLFSize=_DlswNodeVirtualSegmentLFSize_Object((1,3,6,1,4,1,43,45,1,2,34,1,7),_DlswNodeVirtualSegmentLFSize_Type())
dlswNodeVirtualSegmentLFSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeVirtualSegmentLFSize.setStatus(_A)
_DlswNodeLocalAddr_Type=IpAddress
_DlswNodeLocalAddr_Object=MibScalar
dlswNodeLocalAddr=_DlswNodeLocalAddr_Object((1,3,6,1,4,1,43,45,1,2,34,1,8),_DlswNodeLocalAddr_Type())
dlswNodeLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeLocalAddr.setStatus(_A)
class _DlswNodePriority_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5),ValueRangeConstraint(65535,65535))
_DlswNodePriority_Type.__name__=_B
_DlswNodePriority_Object=MibScalar
dlswNodePriority=_DlswNodePriority_Object((1,3,6,1,4,1,43,45,1,2,34,1,9),_DlswNodePriority_Type())
dlswNodePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodePriority.setStatus(_A)
class _DlswNodeInitWindow_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_DlswNodeInitWindow_Type.__name__=_B
_DlswNodeInitWindow_Object=MibScalar
dlswNodeInitWindow=_DlswNodeInitWindow_Object((1,3,6,1,4,1,43,45,1,2,34,1,10),_DlswNodeInitWindow_Type())
dlswNodeInitWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeInitWindow.setStatus(_A)
class _DlswNodeKeepAlive_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_DlswNodeKeepAlive_Type.__name__=_B
_DlswNodeKeepAlive_Object=MibScalar
dlswNodeKeepAlive=_DlswNodeKeepAlive_Object((1,3,6,1,4,1,43,45,1,2,34,1,11),_DlswNodeKeepAlive_Type())
dlswNodeKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeKeepAlive.setStatus(_A)
class _DlswNodeMaxWindow_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_DlswNodeMaxWindow_Type.__name__=_B
_DlswNodeMaxWindow_Object=MibScalar
dlswNodeMaxWindow=_DlswNodeMaxWindow_Object((1,3,6,1,4,1,43,45,1,2,34,1,12),_DlswNodeMaxWindow_Type())
dlswNodeMaxWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeMaxWindow.setStatus(_A)
class _DlswNodePermitDynamic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,65535)));namedValues=NamedValues(*(('permitDynamic',1),('forbidDynamic',2),(_O,65535)))
_DlswNodePermitDynamic_Type.__name__=_B
_DlswNodePermitDynamic_Object=MibScalar
dlswNodePermitDynamic=_DlswNodePermitDynamic_Object((1,3,6,1,4,1,43,45,1,2,34,1,13),_DlswNodePermitDynamic_Type())
dlswNodePermitDynamic.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodePermitDynamic.setStatus(_A)
class _DlswNodeConnTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DlswNodeConnTimeout_Type.__name__=_B
_DlswNodeConnTimeout_Object=MibScalar
dlswNodeConnTimeout=_DlswNodeConnTimeout_Object((1,3,6,1,4,1,43,45,1,2,34,1,14),_DlswNodeConnTimeout_Type())
dlswNodeConnTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeConnTimeout.setStatus(_A)
class _DlswNodeLocalPendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DlswNodeLocalPendTimeout_Type.__name__=_B
_DlswNodeLocalPendTimeout_Object=MibScalar
dlswNodeLocalPendTimeout=_DlswNodeLocalPendTimeout_Object((1,3,6,1,4,1,43,45,1,2,34,1,15),_DlswNodeLocalPendTimeout_Type())
dlswNodeLocalPendTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeLocalPendTimeout.setStatus(_A)
class _DlswNodeRemotePendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DlswNodeRemotePendTimeout_Type.__name__=_B
_DlswNodeRemotePendTimeout_Object=MibScalar
dlswNodeRemotePendTimeout=_DlswNodeRemotePendTimeout_Object((1,3,6,1,4,1,43,45,1,2,34,1,16),_DlswNodeRemotePendTimeout_Type())
dlswNodeRemotePendTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeRemotePendTimeout.setStatus(_A)
class _DlswNodeSnaCacheTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DlswNodeSnaCacheTimeout_Type.__name__=_B
_DlswNodeSnaCacheTimeout_Object=MibScalar
dlswNodeSnaCacheTimeout=_DlswNodeSnaCacheTimeout_Object((1,3,6,1,4,1,43,45,1,2,34,1,17),_DlswNodeSnaCacheTimeout_Type())
dlswNodeSnaCacheTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswNodeSnaCacheTimeout.setStatus(_A)
_DlswTrapControl_ObjectIdentity=ObjectIdentity
dlswTrapControl=_DlswTrapControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,1,20))
class _DlswTrapCntlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_DlswTrapCntlState_Type.__name__=_B
_DlswTrapCntlState_Object=MibScalar
dlswTrapCntlState=_DlswTrapCntlState_Object((1,3,6,1,4,1,43,45,1,2,34,1,20,1),_DlswTrapCntlState_Type())
dlswTrapCntlState.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswTrapCntlState.setStatus(_A)
_DlswTConn_ObjectIdentity=ObjectIdentity
dlswTConn=_DlswTConn_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,2))
_DlswRemotePeerTable_Object=MibTable
dlswRemotePeerTable=_DlswRemotePeerTable_Object((1,3,6,1,4,1,43,45,1,2,34,2,1))
if mibBuilder.loadTexts:dlswRemotePeerTable.setStatus(_A)
_DlswRemotePeerEntry_Object=MibTableRow
dlswRemotePeerEntry=_DlswRemotePeerEntry_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1))
dlswRemotePeerEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:dlswRemotePeerEntry.setStatus(_A)
_DlswRemotePeerAddr_Type=IpAddress
_DlswRemotePeerAddr_Object=MibTableColumn
dlswRemotePeerAddr=_DlswRemotePeerAddr_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,1),_DlswRemotePeerAddr_Type())
dlswRemotePeerAddr.setMaxAccess(_T)
if mibBuilder.loadTexts:dlswRemotePeerAddr.setStatus(_A)
class _DlswRemotePeerVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DlswRemotePeerVersion_Type.__name__=_G
_DlswRemotePeerVersion_Object=MibTableColumn
dlswRemotePeerVersion=_DlswRemotePeerVersion_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,2),_DlswRemotePeerVersion_Type())
dlswRemotePeerVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerVersion.setStatus(_A)
class _DlswRemotePeerVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_DlswRemotePeerVendorID_Type.__name__=_G
_DlswRemotePeerVendorID_Object=MibTableColumn
dlswRemotePeerVendorID=_DlswRemotePeerVendorID_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,3),_DlswRemotePeerVendorID_Type())
dlswRemotePeerVendorID.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerVendorID.setStatus(_A)
_DlswRemotePeerPaceWindInit_Type=Integer32
_DlswRemotePeerPaceWindInit_Object=MibTableColumn
dlswRemotePeerPaceWindInit=_DlswRemotePeerPaceWindInit_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,4),_DlswRemotePeerPaceWindInit_Type())
dlswRemotePeerPaceWindInit.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerPaceWindInit.setStatus(_A)
class _DlswRemotePeerNumOfTcpSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_DlswRemotePeerNumOfTcpSessions_Type.__name__=_B
_DlswRemotePeerNumOfTcpSessions_Object=MibTableColumn
dlswRemotePeerNumOfTcpSessions=_DlswRemotePeerNumOfTcpSessions_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,5),_DlswRemotePeerNumOfTcpSessions_Type())
dlswRemotePeerNumOfTcpSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerNumOfTcpSessions.setStatus(_F)
_DlswRemotePeerVersionString_Type=DisplayString
_DlswRemotePeerVersionString_Object=MibTableColumn
dlswRemotePeerVersionString=_DlswRemotePeerVersionString_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,6),_DlswRemotePeerVersionString_Type())
dlswRemotePeerVersionString.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerVersionString.setStatus(_A)
class _DlswRemotePeerIsConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_DlswRemotePeerIsConfig_Type.__name__=_B
_DlswRemotePeerIsConfig_Object=MibTableColumn
dlswRemotePeerIsConfig=_DlswRemotePeerIsConfig_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,7),_DlswRemotePeerIsConfig_Type())
dlswRemotePeerIsConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerIsConfig.setStatus(_A)
class _DlswRemotePeerSetStateToConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_DlswRemotePeerSetStateToConfig_Type.__name__=_B
_DlswRemotePeerSetStateToConfig_Object=MibTableColumn
dlswRemotePeerSetStateToConfig=_DlswRemotePeerSetStateToConfig_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,8),_DlswRemotePeerSetStateToConfig_Type())
dlswRemotePeerSetStateToConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerSetStateToConfig.setStatus(_F)
class _DlswRemotePeerCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DlswRemotePeerCost_Type.__name__=_B
_DlswRemotePeerCost_Object=MibTableColumn
dlswRemotePeerCost=_DlswRemotePeerCost_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,9),_DlswRemotePeerCost_Type())
dlswRemotePeerCost.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerCost.setStatus(_A)
class _DlswRemotePeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswRemotePeerKeepAlive_Type.__name__=_B
_DlswRemotePeerKeepAlive_Object=MibTableColumn
dlswRemotePeerKeepAlive=_DlswRemotePeerKeepAlive_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,10),_DlswRemotePeerKeepAlive_Type())
dlswRemotePeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerKeepAlive.setStatus(_A)
_DlswRemotePeerLf_Type=LFSize
_DlswRemotePeerLf_Object=MibTableColumn
dlswRemotePeerLf=_DlswRemotePeerLf_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,11),_DlswRemotePeerLf_Type())
dlswRemotePeerLf.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerLf.setStatus(_A)
class _DlswRemotePeerTcpQueneMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_DlswRemotePeerTcpQueneMax_Type.__name__=_B
_DlswRemotePeerTcpQueneMax_Object=MibTableColumn
dlswRemotePeerTcpQueneMax=_DlswRemotePeerTcpQueneMax_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,12),_DlswRemotePeerTcpQueneMax_Type())
dlswRemotePeerTcpQueneMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerTcpQueneMax.setStatus(_A)
class _DlswRemotePeerHaveBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_DlswRemotePeerHaveBackup_Type.__name__=_B
_DlswRemotePeerHaveBackup_Object=MibTableColumn
dlswRemotePeerHaveBackup=_DlswRemotePeerHaveBackup_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,13),_DlswRemotePeerHaveBackup_Type())
dlswRemotePeerHaveBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerHaveBackup.setStatus(_A)
class _DlswRemotePeerIsBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_DlswRemotePeerIsBackup_Type.__name__=_B
_DlswRemotePeerIsBackup_Object=MibTableColumn
dlswRemotePeerIsBackup=_DlswRemotePeerIsBackup_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,14),_DlswRemotePeerIsBackup_Type())
dlswRemotePeerIsBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerIsBackup.setStatus(_A)
_DlswRemotePeerBackupAddr_Type=IpAddress
_DlswRemotePeerBackupAddr_Object=MibTableColumn
dlswRemotePeerBackupAddr=_DlswRemotePeerBackupAddr_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,15),_DlswRemotePeerBackupAddr_Type())
dlswRemotePeerBackupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerBackupAddr.setStatus(_A)
class _DlswRemotePeerLinger_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_DlswRemotePeerLinger_Type.__name__=_B
_DlswRemotePeerLinger_Object=MibTableColumn
dlswRemotePeerLinger=_DlswRemotePeerLinger_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,16),_DlswRemotePeerLinger_Type())
dlswRemotePeerLinger.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerLinger.setStatus(_A)
class _DlswRemotePeerLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('connecting',1),('initCapExchange',2),(_U,3),('quiescing',4),('disconnecting',5),(_V,6)))
_DlswRemotePeerLinkState_Type.__name__=_B
_DlswRemotePeerLinkState_Object=MibTableColumn
dlswRemotePeerLinkState=_DlswRemotePeerLinkState_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,17),_DlswRemotePeerLinkState_Type())
dlswRemotePeerLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerLinkState.setStatus(_A)
_DlswRemotePeerRecvPacks_Type=Counter32
_DlswRemotePeerRecvPacks_Object=MibTableColumn
dlswRemotePeerRecvPacks=_DlswRemotePeerRecvPacks_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,18),_DlswRemotePeerRecvPacks_Type())
dlswRemotePeerRecvPacks.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerRecvPacks.setStatus(_A)
_DlswRemotePeerSendPacks_Type=Counter32
_DlswRemotePeerSendPacks_Object=MibTableColumn
dlswRemotePeerSendPacks=_DlswRemotePeerSendPacks_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,19),_DlswRemotePeerSendPacks_Type())
dlswRemotePeerSendPacks.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerSendPacks.setStatus(_A)
_DlswRemotePeerDrops_Type=Counter32
_DlswRemotePeerDrops_Object=MibTableColumn
dlswRemotePeerDrops=_DlswRemotePeerDrops_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,20),_DlswRemotePeerDrops_Type())
dlswRemotePeerDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerDrops.setStatus(_A)
_DlswRemotePeerUptime_Type=Counter32
_DlswRemotePeerUptime_Object=MibTableColumn
dlswRemotePeerUptime=_DlswRemotePeerUptime_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,21),_DlswRemotePeerUptime_Type())
dlswRemotePeerUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswRemotePeerUptime.setStatus(_A)
_DlswRemotePeerEntryStatus_Type=EntryStatus
_DlswRemotePeerEntryStatus_Object=MibTableColumn
dlswRemotePeerEntryStatus=_DlswRemotePeerEntryStatus_Object((1,3,6,1,4,1,43,45,1,2,34,2,1,1,22),_DlswRemotePeerEntryStatus_Type())
dlswRemotePeerEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswRemotePeerEntryStatus.setStatus(_A)
_DlswBridgeGroup_ObjectIdentity=ObjectIdentity
dlswBridgeGroup=_DlswBridgeGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,3))
_DlswBridgeTable_Object=MibTable
dlswBridgeTable=_DlswBridgeTable_Object((1,3,6,1,4,1,43,45,1,2,34,3,1))
if mibBuilder.loadTexts:dlswBridgeTable.setStatus(_A)
_DlswBridgeEntry_Object=MibTableRow
dlswBridgeEntry=_DlswBridgeEntry_Object((1,3,6,1,4,1,43,45,1,2,34,3,1,1))
dlswBridgeEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:dlswBridgeEntry.setStatus(_A)
class _DlswBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_DlswBridgeNum_Type.__name__=_B
_DlswBridgeNum_Object=MibTableColumn
dlswBridgeNum=_DlswBridgeNum_Object((1,3,6,1,4,1,43,45,1,2,34,3,1,1,1),_DlswBridgeNum_Type())
dlswBridgeNum.setMaxAccess(_M)
if mibBuilder.loadTexts:dlswBridgeNum.setStatus(_A)
_DlswBridgeStatus_Type=CreateLineFlag
_DlswBridgeStatus_Object=MibTableColumn
dlswBridgeStatus=_DlswBridgeStatus_Object((1,3,6,1,4,1,43,45,1,2,34,3,1,1,2),_DlswBridgeStatus_Type())
dlswBridgeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswBridgeStatus.setStatus(_A)
_DlswBridgeIfTable_Object=MibTable
dlswBridgeIfTable=_DlswBridgeIfTable_Object((1,3,6,1,4,1,43,45,1,2,34,3,2))
if mibBuilder.loadTexts:dlswBridgeIfTable.setStatus(_A)
_DlswBridgeIfEntry_Object=MibTableRow
dlswBridgeIfEntry=_DlswBridgeIfEntry_Object((1,3,6,1,4,1,43,45,1,2,34,3,2,1))
dlswBridgeIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dlswBridgeIfEntry.setStatus(_A)
class _DlswBridgeIfBriGru_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_DlswBridgeIfBriGru_Type.__name__=_B
_DlswBridgeIfBriGru_Object=MibTableColumn
dlswBridgeIfBriGru=_DlswBridgeIfBriGru_Object((1,3,6,1,4,1,43,45,1,2,34,3,2,1,1),_DlswBridgeIfBriGru_Type())
dlswBridgeIfBriGru.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswBridgeIfBriGru.setStatus(_A)
_DlswBridgeIfName_Type=DisplayString
_DlswBridgeIfName_Object=MibTableColumn
dlswBridgeIfName=_DlswBridgeIfName_Object((1,3,6,1,4,1,43,45,1,2,34,3,2,1,2),_DlswBridgeIfName_Type())
dlswBridgeIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswBridgeIfName.setStatus(_A)
_DlswBridgeIfStatus_Type=EntryStatus
_DlswBridgeIfStatus_Object=MibTableColumn
dlswBridgeIfStatus=_DlswBridgeIfStatus_Object((1,3,6,1,4,1,43,45,1,2,34,3,2,1,3),_DlswBridgeIfStatus_Type())
dlswBridgeIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswBridgeIfStatus.setStatus(_A)
_DlswLocDirectory_ObjectIdentity=ObjectIdentity
dlswLocDirectory=_DlswLocDirectory_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,4))
_DlswLocMacTable_Object=MibTable
dlswLocMacTable=_DlswLocMacTable_Object((1,3,6,1,4,1,43,45,1,2,34,4,1))
if mibBuilder.loadTexts:dlswLocMacTable.setStatus(_A)
_DlswLocMacEntry_Object=MibTableRow
dlswLocMacEntry=_DlswLocMacEntry_Object((1,3,6,1,4,1,43,45,1,2,34,4,1,1))
dlswLocMacEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:dlswLocMacEntry.setStatus(_A)
_DlswLocMacHashIndex_Type=Integer32
_DlswLocMacHashIndex_Object=MibTableColumn
dlswLocMacHashIndex=_DlswLocMacHashIndex_Object((1,3,6,1,4,1,43,45,1,2,34,4,1,1,1),_DlswLocMacHashIndex_Type())
dlswLocMacHashIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:dlswLocMacHashIndex.setStatus(_A)
_DlswLocMacHashIndexSeqNum_Type=Integer32
_DlswLocMacHashIndexSeqNum_Object=MibTableColumn
dlswLocMacHashIndexSeqNum=_DlswLocMacHashIndexSeqNum_Object((1,3,6,1,4,1,43,45,1,2,34,4,1,1,2),_DlswLocMacHashIndexSeqNum_Type())
dlswLocMacHashIndexSeqNum.setMaxAccess(_M)
if mibBuilder.loadTexts:dlswLocMacHashIndexSeqNum.setStatus(_A)
_DlswLocMacMac_Type=MacAddressNC
_DlswLocMacMac_Object=MibTableColumn
dlswLocMacMac=_DlswLocMacMac_Object((1,3,6,1,4,1,43,45,1,2,34,4,1,1,3),_DlswLocMacMac_Type())
dlswLocMacMac.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswLocMacMac.setStatus(_A)
_DlswLocMacLocalInterfaceName_Type=DisplayString
_DlswLocMacLocalInterfaceName_Object=MibTableColumn
dlswLocMacLocalInterfaceName=_DlswLocMacLocalInterfaceName_Object((1,3,6,1,4,1,43,45,1,2,34,4,1,1,4),_DlswLocMacLocalInterfaceName_Type())
dlswLocMacLocalInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswLocMacLocalInterfaceName.setStatus(_A)
_DlswCircuit_ObjectIdentity=ObjectIdentity
dlswCircuit=_DlswCircuit_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,5))
_DlswCircuitTable_Object=MibTable
dlswCircuitTable=_DlswCircuitTable_Object((1,3,6,1,4,1,43,45,1,2,34,5,1))
if mibBuilder.loadTexts:dlswCircuitTable.setStatus(_A)
_DlswCircuitEntry_Object=MibTableRow
dlswCircuitEntry=_DlswCircuitEntry_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1))
dlswCircuitEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:dlswCircuitEntry.setStatus(_A)
_DlswCircuitS1CircuitId_Type=Integer32
_DlswCircuitS1CircuitId_Object=MibTableColumn
dlswCircuitS1CircuitId=_DlswCircuitS1CircuitId_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,1),_DlswCircuitS1CircuitId_Type())
dlswCircuitS1CircuitId.setMaxAccess(_T)
if mibBuilder.loadTexts:dlswCircuitS1CircuitId.setStatus(_A)
_DlswCircuitS1Mac_Type=MacAddressNC
_DlswCircuitS1Mac_Object=MibTableColumn
dlswCircuitS1Mac=_DlswCircuitS1Mac_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,2),_DlswCircuitS1Mac_Type())
dlswCircuitS1Mac.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS1Mac.setStatus(_A)
class _DlswCircuitS1Sap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_DlswCircuitS1Sap_Type.__name__=_G
_DlswCircuitS1Sap_Object=MibTableColumn
dlswCircuitS1Sap=_DlswCircuitS1Sap_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,3),_DlswCircuitS1Sap_Type())
dlswCircuitS1Sap.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS1Sap.setStatus(_A)
_DlswCircuitS2Mac_Type=MacAddressNC
_DlswCircuitS2Mac_Object=MibTableColumn
dlswCircuitS2Mac=_DlswCircuitS2Mac_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,4),_DlswCircuitS2Mac_Type())
dlswCircuitS2Mac.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS2Mac.setStatus(_A)
class _DlswCircuitS2Sap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_DlswCircuitS2Sap_Type.__name__=_G
_DlswCircuitS2Sap_Object=MibTableColumn
dlswCircuitS2Sap=_DlswCircuitS2Sap_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,5),_DlswCircuitS2Sap_Type())
dlswCircuitS2Sap.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS2Sap.setStatus(_A)
class _DlswCircuitS1IfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DlswCircuitS1IfIndex_Type.__name__=_B
_DlswCircuitS1IfIndex_Object=MibTableColumn
dlswCircuitS1IfIndex=_DlswCircuitS1IfIndex_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,6),_DlswCircuitS1IfIndex_Type())
dlswCircuitS1IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS1IfIndex.setStatus(_A)
_DlswCircuitS1Ifname_Type=DisplayString
_DlswCircuitS1Ifname_Object=MibTableColumn
dlswCircuitS1Ifname=_DlswCircuitS1Ifname_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,7),_DlswCircuitS1Ifname_Type())
dlswCircuitS1Ifname.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS1Ifname.setStatus(_A)
_DlswCircuitS1DlcType_Type=DlcType
_DlswCircuitS1DlcType_Object=MibTableColumn
dlswCircuitS1DlcType=_DlswCircuitS1DlcType_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,8),_DlswCircuitS1DlcType_Type())
dlswCircuitS1DlcType.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS1DlcType.setStatus(_A)
_DlswCircuitS2Location_Type=EndStationLocation
_DlswCircuitS2Location_Object=MibTableColumn
dlswCircuitS2Location=_DlswCircuitS2Location_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,9),_DlswCircuitS2Location_Type())
dlswCircuitS2Location.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS2Location.setStatus(_F)
_DlswCircuitS2TAddress_Type=IpAddress
_DlswCircuitS2TAddress_Object=MibTableColumn
dlswCircuitS2TAddress=_DlswCircuitS2TAddress_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,10),_DlswCircuitS2TAddress_Type())
dlswCircuitS2TAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS2TAddress.setStatus(_A)
_DlswCircuitS2CircuitId_Type=Integer32
_DlswCircuitS2CircuitId_Object=MibTableColumn
dlswCircuitS2CircuitId=_DlswCircuitS2CircuitId_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,11),_DlswCircuitS2CircuitId_Type())
dlswCircuitS2CircuitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitS2CircuitId.setStatus(_A)
class _DlswCircuitOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('s1',1),('s2',2)))
_DlswCircuitOrigin_Type.__name__=_B
_DlswCircuitOrigin_Object=MibTableColumn
dlswCircuitOrigin=_DlswCircuitOrigin_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,12),_DlswCircuitOrigin_Type())
dlswCircuitOrigin.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitOrigin.setStatus(_A)
_DlswCircuitEntryTime_Type=TimeTicks
_DlswCircuitEntryTime_Object=MibTableColumn
dlswCircuitEntryTime=_DlswCircuitEntryTime_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,13),_DlswCircuitEntryTime_Type())
dlswCircuitEntryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitEntryTime.setStatus(_A)
if mibBuilder.loadTexts:dlswCircuitEntryTime.setUnits(_Z)
_DlswCircuitStateTime_Type=TimeTicks
_DlswCircuitStateTime_Object=MibTableColumn
dlswCircuitStateTime=_DlswCircuitStateTime_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,14),_DlswCircuitStateTime_Type())
dlswCircuitStateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitStateTime.setStatus(_A)
if mibBuilder.loadTexts:dlswCircuitStateTime.setUnits(_Z)
class _DlswCircuitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_V,1),('circuitStart',2),('resolvePending',3),('circuitPending',4),('circuitEstablished',5),('connectPending',6),('contactPending',7),(_U,8),('disconnectPending',9),('haltPending',10),('haltPendingNoack',11),('circuitRestart',12),('restartPending',13)))
_DlswCircuitState_Type.__name__=_B
_DlswCircuitState_Object=MibTableColumn
dlswCircuitState=_DlswCircuitState_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,15),_DlswCircuitState_Type())
dlswCircuitState.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitState.setStatus(_A)
class _DlswCircuitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unsupported',1),('low',2),('medium',3),('high',4),('highest',5)))
_DlswCircuitPriority_Type.__name__=_B
_DlswCircuitPriority_Object=MibTableColumn
dlswCircuitPriority=_DlswCircuitPriority_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,16),_DlswCircuitPriority_Type())
dlswCircuitPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitPriority.setStatus(_F)
class _DlswCircuitFCSendGrantedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCSendGrantedUnits_Type.__name__=_B
_DlswCircuitFCSendGrantedUnits_Object=MibTableColumn
dlswCircuitFCSendGrantedUnits=_DlswCircuitFCSendGrantedUnits_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,17),_DlswCircuitFCSendGrantedUnits_Type())
dlswCircuitFCSendGrantedUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCSendGrantedUnits.setStatus(_A)
class _DlswCircuitFCSendCurrentWndw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCSendCurrentWndw_Type.__name__=_B
_DlswCircuitFCSendCurrentWndw_Object=MibTableColumn
dlswCircuitFCSendCurrentWndw=_DlswCircuitFCSendCurrentWndw_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,18),_DlswCircuitFCSendCurrentWndw_Type())
dlswCircuitFCSendCurrentWndw.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCSendCurrentWndw.setStatus(_A)
class _DlswCircuitFCRecvGrantedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCRecvGrantedUnits_Type.__name__=_B
_DlswCircuitFCRecvGrantedUnits_Object=MibTableColumn
dlswCircuitFCRecvGrantedUnits=_DlswCircuitFCRecvGrantedUnits_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,19),_DlswCircuitFCRecvGrantedUnits_Type())
dlswCircuitFCRecvGrantedUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCRecvGrantedUnits.setStatus(_A)
class _DlswCircuitFCRecvCurrentWndw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCRecvCurrentWndw_Type.__name__=_B
_DlswCircuitFCRecvCurrentWndw_Object=MibTableColumn
dlswCircuitFCRecvCurrentWndw=_DlswCircuitFCRecvCurrentWndw_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,20),_DlswCircuitFCRecvCurrentWndw_Type())
dlswCircuitFCRecvCurrentWndw.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCRecvCurrentWndw.setStatus(_A)
_DlswCircuitFCLargestRecvGranted_Type=Gauge32
_DlswCircuitFCLargestRecvGranted_Object=MibTableColumn
dlswCircuitFCLargestRecvGranted=_DlswCircuitFCLargestRecvGranted_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,21),_DlswCircuitFCLargestRecvGranted_Type())
dlswCircuitFCLargestRecvGranted.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCLargestRecvGranted.setStatus(_F)
_DlswCircuitFCLargestSendGranted_Type=Gauge32
_DlswCircuitFCLargestSendGranted_Object=MibTableColumn
dlswCircuitFCLargestSendGranted=_DlswCircuitFCLargestSendGranted_Object((1,3,6,1,4,1,43,45,1,2,34,5,1,1,22),_DlswCircuitFCLargestSendGranted_Type())
dlswCircuitFCLargestSendGranted.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswCircuitFCLargestSendGranted.setStatus(_F)
_DlswSdlc_ObjectIdentity=ObjectIdentity
dlswSdlc=_DlswSdlc_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,6))
_DlswSdlcPortTable_Object=MibTable
dlswSdlcPortTable=_DlswSdlcPortTable_Object((1,3,6,1,4,1,43,45,1,2,34,6,1))
if mibBuilder.loadTexts:dlswSdlcPortTable.setStatus(_A)
_DlswSdlcPortEntry_Object=MibTableRow
dlswSdlcPortEntry=_DlswSdlcPortEntry_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1))
dlswSdlcPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dlswSdlcPortEntry.setStatus(_A)
_DlswSdlcPortSerialName_Type=DisplayString
_DlswSdlcPortSerialName_Object=MibTableColumn
dlswSdlcPortSerialName=_DlswSdlcPortSerialName_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,1),_DlswSdlcPortSerialName_Type())
dlswSdlcPortSerialName.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswSdlcPortSerialName.setStatus(_A)
class _DlswSdlcPortEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sdlc',1),('ppp',2),(_N,3)))
_DlswSdlcPortEncap_Type.__name__=_B
_DlswSdlcPortEncap_Object=MibTableColumn
dlswSdlcPortEncap=_DlswSdlcPortEncap_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,2),_DlswSdlcPortEncap_Type())
dlswSdlcPortEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:dlswSdlcPortEncap.setStatus(_A)
class _DlswSdlcPortRole_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('seconday',2),('norole',3)))
_DlswSdlcPortRole_Type.__name__=_B
_DlswSdlcPortRole_Object=MibTableColumn
dlswSdlcPortRole=_DlswSdlcPortRole_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,3),_DlswSdlcPortRole_Type())
dlswSdlcPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortRole.setStatus(_A)
_DlswSdlcPortVmac_Type=MacAddressNC
_DlswSdlcPortVmac_Object=MibTableColumn
dlswSdlcPortVmac=_DlswSdlcPortVmac_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,4),_DlswSdlcPortVmac_Type())
dlswSdlcPortVmac.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortVmac.setStatus(_A)
class _DlswSdlcPortHoldq_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,255))
_DlswSdlcPortHoldq_Type.__name__=_B
_DlswSdlcPortHoldq_Object=MibTableColumn
dlswSdlcPortHoldq=_DlswSdlcPortHoldq_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,5),_DlswSdlcPortHoldq_Type())
dlswSdlcPortHoldq.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortHoldq.setStatus(_A)
class _DlswSdlcPortK_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_DlswSdlcPortK_Type.__name__=_B
_DlswSdlcPortK_Object=MibTableColumn
dlswSdlcPortK=_DlswSdlcPortK_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,6),_DlswSdlcPortK_Type())
dlswSdlcPortK.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortK.setStatus(_A)
class _DlswSdlcPortModule_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_DlswSdlcPortModule_Type.__name__=_B
_DlswSdlcPortModule_Object=MibTableColumn
dlswSdlcPortModule=_DlswSdlcPortModule_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,7),_DlswSdlcPortModule_Type())
dlswSdlcPortModule.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortModule.setStatus(_A)
class _DlswSdlcPortN1_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17680))
_DlswSdlcPortN1_Type.__name__=_B
_DlswSdlcPortN1_Object=MibTableColumn
dlswSdlcPortN1=_DlswSdlcPortN1_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,8),_DlswSdlcPortN1_Type())
dlswSdlcPortN1.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortN1.setStatus(_A)
class _DlswSdlcPortN2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DlswSdlcPortN2_Type.__name__=_B
_DlswSdlcPortN2_Object=MibTableColumn
dlswSdlcPortN2=_DlswSdlcPortN2_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,9),_DlswSdlcPortN2_Type())
dlswSdlcPortN2.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortN2.setStatus(_A)
class _DlswSdlcPortPollPauseTimer_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_DlswSdlcPortPollPauseTimer_Type.__name__=_B
_DlswSdlcPortPollPauseTimer_Object=MibTableColumn
dlswSdlcPortPollPauseTimer=_DlswSdlcPortPollPauseTimer_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,10),_DlswSdlcPortPollPauseTimer_Type())
dlswSdlcPortPollPauseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortPollPauseTimer.setStatus(_A)
class _DlswSdlcPortSimultaneousEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DlswSdlcPortSimultaneousEnable_Type.__name__=_B
_DlswSdlcPortSimultaneousEnable_Object=MibTableColumn
dlswSdlcPortSimultaneousEnable=_DlswSdlcPortSimultaneousEnable_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,11),_DlswSdlcPortSimultaneousEnable_Type())
dlswSdlcPortSimultaneousEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortSimultaneousEnable.setStatus(_A)
class _DlswSdlcPortT1_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswSdlcPortT1_Type.__name__=_B
_DlswSdlcPortT1_Object=MibTableColumn
dlswSdlcPortT1=_DlswSdlcPortT1_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,12),_DlswSdlcPortT1_Type())
dlswSdlcPortT1.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortT1.setStatus(_A)
class _DlswSdlcPortT2_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswSdlcPortT2_Type.__name__=_B
_DlswSdlcPortT2_Object=MibTableColumn
dlswSdlcPortT2=_DlswSdlcPortT2_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,13),_DlswSdlcPortT2_Type())
dlswSdlcPortT2.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortT2.setStatus(_A)
class _DlswSdlcPortNrziEncoding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DlswSdlcPortNrziEncoding_Type.__name__=_B
_DlswSdlcPortNrziEncoding_Object=MibTableColumn
dlswSdlcPortNrziEncoding=_DlswSdlcPortNrziEncoding_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,14),_DlswSdlcPortNrziEncoding_Type())
dlswSdlcPortNrziEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortNrziEncoding.setStatus(_F)
class _DlswSdlcPortIdleMarkEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DlswSdlcPortIdleMarkEnable_Type.__name__=_B
_DlswSdlcPortIdleMarkEnable_Object=MibTableColumn
dlswSdlcPortIdleMarkEnable=_DlswSdlcPortIdleMarkEnable_Object((1,3,6,1,4,1,43,45,1,2,34,6,1,1,15),_DlswSdlcPortIdleMarkEnable_Type())
dlswSdlcPortIdleMarkEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcPortIdleMarkEnable.setStatus(_F)
_DlswSdlcLsTable_Object=MibTable
dlswSdlcLsTable=_DlswSdlcLsTable_Object((1,3,6,1,4,1,43,45,1,2,34,6,2))
if mibBuilder.loadTexts:dlswSdlcLsTable.setStatus(_A)
_DlswSdlcLsEntry_Object=MibTableRow
dlswSdlcLsEntry=_DlswSdlcLsEntry_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1))
dlswSdlcLsEntry.setIndexNames((0,_H,_I),(0,_E,_a))
if mibBuilder.loadTexts:dlswSdlcLsEntry.setStatus(_A)
class _DlswSdlcLsAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DlswSdlcLsAddress_Type.__name__=_B
_DlswSdlcLsAddress_Object=MibTableColumn
dlswSdlcLsAddress=_DlswSdlcLsAddress_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,1),_DlswSdlcLsAddress_Type())
dlswSdlcLsAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:dlswSdlcLsAddress.setStatus(_A)
class _DlswSdlcLsLocalId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DlswSdlcLsLocalId_Type.__name__=_B
_DlswSdlcLsLocalId_Object=MibTableColumn
dlswSdlcLsLocalId=_DlswSdlcLsLocalId_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,2),_DlswSdlcLsLocalId_Type())
dlswSdlcLsLocalId.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcLsLocalId.setStatus(_A)
_DlswSdlcLsRemoteMac_Type=MacAddressNC
_DlswSdlcLsRemoteMac_Object=MibTableColumn
dlswSdlcLsRemoteMac=_DlswSdlcLsRemoteMac_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,3),_DlswSdlcLsRemoteMac_Type())
dlswSdlcLsRemoteMac.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcLsRemoteMac.setStatus(_A)
class _DlswSdlcLsSsap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DlswSdlcLsSsap_Type.__name__=_B
_DlswSdlcLsSsap_Object=MibTableColumn
dlswSdlcLsSsap=_DlswSdlcLsSsap_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,4),_DlswSdlcLsSsap_Type())
dlswSdlcLsSsap.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcLsSsap.setStatus(_A)
class _DlswSdlcLsDsap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DlswSdlcLsDsap_Type.__name__=_B
_DlswSdlcLsDsap_Object=MibTableColumn
dlswSdlcLsDsap=_DlswSdlcLsDsap_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,5),_DlswSdlcLsDsap_Type())
dlswSdlcLsDsap.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcLsDsap.setStatus(_A)
_DlswSdlcLsStatus_Type=EntryStatus
_DlswSdlcLsStatus_Object=MibTableColumn
dlswSdlcLsStatus=_DlswSdlcLsStatus_Object((1,3,6,1,4,1,43,45,1,2,34,6,2,1,6),_DlswSdlcLsStatus_Type())
dlswSdlcLsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswSdlcLsStatus.setStatus(_A)
_DlswLlc2_ObjectIdentity=ObjectIdentity
dlswLlc2=_DlswLlc2_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,7))
_DlswLlc2PortTable_Object=MibTable
dlswLlc2PortTable=_DlswLlc2PortTable_Object((1,3,6,1,4,1,43,45,1,2,34,7,1))
if mibBuilder.loadTexts:dlswLlc2PortTable.setStatus(_A)
_DlswLlc2PortEntry_Object=MibTableRow
dlswLlc2PortEntry=_DlswLlc2PortEntry_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1))
dlswLlc2PortEntry.setIndexNames((0,_H,_I),(0,_E,_b))
if mibBuilder.loadTexts:dlswLlc2PortEntry.setStatus(_A)
class _DlswLLC2PortAckDelayTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswLLC2PortAckDelayTime_Type.__name__=_B
_DlswLLC2PortAckDelayTime_Object=MibTableColumn
dlswLLC2PortAckDelayTime=_DlswLLC2PortAckDelayTime_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,1),_DlswLLC2PortAckDelayTime_Type())
dlswLLC2PortAckDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortAckDelayTime.setStatus(_A)
class _DlswLLC2PortAckMax_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DlswLLC2PortAckMax_Type.__name__=_B
_DlswLLC2PortAckMax_Object=MibTableColumn
dlswLLC2PortAckMax=_DlswLLC2PortAckMax_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,2),_DlswLLC2PortAckMax_Type())
dlswLLC2PortAckMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortAckMax.setStatus(_A)
class _DlswLLC2PortLocalWnd_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DlswLLC2PortLocalWnd_Type.__name__=_B
_DlswLLC2PortLocalWnd_Object=MibTableColumn
dlswLLC2PortLocalWnd=_DlswLLC2PortLocalWnd_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,3),_DlswLLC2PortLocalWnd_Type())
dlswLLC2PortLocalWnd.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortLocalWnd.setStatus(_A)
class _DlswLLC2PortModulus_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_DlswLLC2PortModulus_Type.__name__=_B
_DlswLLC2PortModulus_Object=MibTableColumn
dlswLLC2PortModulus=_DlswLLC2PortModulus_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,4),_DlswLLC2PortModulus_Type())
dlswLLC2PortModulus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortModulus.setStatus(_A)
class _DlswLLC2PortN2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DlswLLC2PortN2_Type.__name__=_B
_DlswLLC2PortN2_Object=MibTableColumn
dlswLLC2PortN2=_DlswLLC2PortN2_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,5),_DlswLLC2PortN2_Type())
dlswLLC2PortN2.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortN2.setStatus(_A)
class _DlswLLC2PortT1_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswLLC2PortT1_Type.__name__=_B
_DlswLLC2PortT1_Object=MibTableColumn
dlswLLC2PortT1=_DlswLLC2PortT1_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,6),_DlswLLC2PortT1_Type())
dlswLLC2PortT1.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortT1.setStatus(_A)
class _DlswLLC2PortTbusyTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswLLC2PortTbusyTime_Type.__name__=_B
_DlswLLC2PortTbusyTime_Object=MibTableColumn
dlswLLC2PortTbusyTime=_DlswLLC2PortTbusyTime_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,7),_DlswLLC2PortTbusyTime_Type())
dlswLLC2PortTbusyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortTbusyTime.setStatus(_A)
class _DlswLLC2PortTpfTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswLLC2PortTpfTime_Type.__name__=_B
_DlswLLC2PortTpfTime_Object=MibTableColumn
dlswLLC2PortTpfTime=_DlswLLC2PortTpfTime_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,8),_DlswLLC2PortTpfTime_Type())
dlswLLC2PortTpfTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortTpfTime.setStatus(_A)
class _DlswLLC2PortTrejTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_DlswLLC2PortTrejTime_Type.__name__=_B
_DlswLLC2PortTrejTime_Object=MibTableColumn
dlswLLC2PortTrejTime=_DlswLLC2PortTrejTime_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,9),_DlswLLC2PortTrejTime_Type())
dlswLLC2PortTrejTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortTrejTime.setStatus(_A)
class _DlswLLC2PortTxqMax_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_DlswLLC2PortTxqMax_Type.__name__=_B
_DlswLLC2PortTxqMax_Object=MibTableColumn
dlswLLC2PortTxqMax=_DlswLLC2PortTxqMax_Object((1,3,6,1,4,1,43,45,1,2,34,7,1,1,10),_DlswLLC2PortTxqMax_Type())
dlswLLC2PortTxqMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dlswLLC2PortTxqMax.setStatus(_A)
_DlswTraps_ObjectIdentity=ObjectIdentity
dlswTraps=_DlswTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,8))
_DlswTrapsV2_ObjectIdentity=ObjectIdentity
dlswTrapsV2=_DlswTrapsV2_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,34,8,0))
dlswTrapTConnPartnerReject=NotificationType((1,3,6,1,4,1,43,45,1,2,34,8,0,1))
dlswTrapTConnPartnerReject.setObjects((_E,_J))
if mibBuilder.loadTexts:dlswTrapTConnPartnerReject.setStatus(_A)
dlswTrapTConnChangeState=NotificationType((1,3,6,1,4,1,43,45,1,2,34,8,0,2))
dlswTrapTConnChangeState.setObjects(*((_E,_J),(_E,_c)))
if mibBuilder.loadTexts:dlswTrapTConnChangeState.setStatus(_A)
dlswTrapCircuitChangeState=NotificationType((1,3,6,1,4,1,43,45,1,2,34,8,0,3))
dlswTrapCircuitChangeState.setObjects(*((_E,_P),(_E,_d),(_E,_e),(_E,_f),(_E,_g),(_E,_h)))
if mibBuilder.loadTexts:dlswTrapCircuitChangeState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddressNC':MacAddressNC,'EndStationLocation':EndStationLocation,'DlcType':DlcType,_S:LFSize,'CreateLineFlag':CreateLineFlag,'EntryStatus':EntryStatus,'dlsw':dlsw,'dlswNode':dlswNode,'dlswNodeVersion':dlswNodeVersion,'dlswNodeVendorID':dlswNodeVendorID,'dlswNodeVersionString':dlswNodeVersionString,'dlswNodeStdPacingSupport':dlswNodeStdPacingSupport,'dlswNodeStatus':dlswNodeStatus,'dlswNodeUpTime':dlswNodeUpTime,'dlswNodeVirtualSegmentLFSize':dlswNodeVirtualSegmentLFSize,'dlswNodeLocalAddr':dlswNodeLocalAddr,'dlswNodePriority':dlswNodePriority,'dlswNodeInitWindow':dlswNodeInitWindow,'dlswNodeKeepAlive':dlswNodeKeepAlive,'dlswNodeMaxWindow':dlswNodeMaxWindow,'dlswNodePermitDynamic':dlswNodePermitDynamic,'dlswNodeConnTimeout':dlswNodeConnTimeout,'dlswNodeLocalPendTimeout':dlswNodeLocalPendTimeout,'dlswNodeRemotePendTimeout':dlswNodeRemotePendTimeout,'dlswNodeSnaCacheTimeout':dlswNodeSnaCacheTimeout,'dlswTrapControl':dlswTrapControl,'dlswTrapCntlState':dlswTrapCntlState,'dlswTConn':dlswTConn,'dlswRemotePeerTable':dlswRemotePeerTable,'dlswRemotePeerEntry':dlswRemotePeerEntry,_J:dlswRemotePeerAddr,'dlswRemotePeerVersion':dlswRemotePeerVersion,'dlswRemotePeerVendorID':dlswRemotePeerVendorID,'dlswRemotePeerPaceWindInit':dlswRemotePeerPaceWindInit,'dlswRemotePeerNumOfTcpSessions':dlswRemotePeerNumOfTcpSessions,'dlswRemotePeerVersionString':dlswRemotePeerVersionString,'dlswRemotePeerIsConfig':dlswRemotePeerIsConfig,'dlswRemotePeerSetStateToConfig':dlswRemotePeerSetStateToConfig,'dlswRemotePeerCost':dlswRemotePeerCost,'dlswRemotePeerKeepAlive':dlswRemotePeerKeepAlive,'dlswRemotePeerLf':dlswRemotePeerLf,'dlswRemotePeerTcpQueneMax':dlswRemotePeerTcpQueneMax,'dlswRemotePeerHaveBackup':dlswRemotePeerHaveBackup,'dlswRemotePeerIsBackup':dlswRemotePeerIsBackup,'dlswRemotePeerBackupAddr':dlswRemotePeerBackupAddr,'dlswRemotePeerLinger':dlswRemotePeerLinger,_c:dlswRemotePeerLinkState,'dlswRemotePeerRecvPacks':dlswRemotePeerRecvPacks,'dlswRemotePeerSendPacks':dlswRemotePeerSendPacks,'dlswRemotePeerDrops':dlswRemotePeerDrops,'dlswRemotePeerUptime':dlswRemotePeerUptime,'dlswRemotePeerEntryStatus':dlswRemotePeerEntryStatus,'dlswBridgeGroup':dlswBridgeGroup,'dlswBridgeTable':dlswBridgeTable,'dlswBridgeEntry':dlswBridgeEntry,_W:dlswBridgeNum,'dlswBridgeStatus':dlswBridgeStatus,'dlswBridgeIfTable':dlswBridgeIfTable,'dlswBridgeIfEntry':dlswBridgeIfEntry,_b:dlswBridgeIfBriGru,'dlswBridgeIfName':dlswBridgeIfName,'dlswBridgeIfStatus':dlswBridgeIfStatus,'dlswLocDirectory':dlswLocDirectory,'dlswLocMacTable':dlswLocMacTable,'dlswLocMacEntry':dlswLocMacEntry,_X:dlswLocMacHashIndex,_Y:dlswLocMacHashIndexSeqNum,'dlswLocMacMac':dlswLocMacMac,'dlswLocMacLocalInterfaceName':dlswLocMacLocalInterfaceName,'dlswCircuit':dlswCircuit,'dlswCircuitTable':dlswCircuitTable,'dlswCircuitEntry':dlswCircuitEntry,_P:dlswCircuitS1CircuitId,_e:dlswCircuitS1Mac,_f:dlswCircuitS1Sap,_g:dlswCircuitS2Mac,_h:dlswCircuitS2Sap,'dlswCircuitS1IfIndex':dlswCircuitS1IfIndex,'dlswCircuitS1Ifname':dlswCircuitS1Ifname,'dlswCircuitS1DlcType':dlswCircuitS1DlcType,'dlswCircuitS2Location':dlswCircuitS2Location,'dlswCircuitS2TAddress':dlswCircuitS2TAddress,'dlswCircuitS2CircuitId':dlswCircuitS2CircuitId,'dlswCircuitOrigin':dlswCircuitOrigin,'dlswCircuitEntryTime':dlswCircuitEntryTime,'dlswCircuitStateTime':dlswCircuitStateTime,_d:dlswCircuitState,'dlswCircuitPriority':dlswCircuitPriority,'dlswCircuitFCSendGrantedUnits':dlswCircuitFCSendGrantedUnits,'dlswCircuitFCSendCurrentWndw':dlswCircuitFCSendCurrentWndw,'dlswCircuitFCRecvGrantedUnits':dlswCircuitFCRecvGrantedUnits,'dlswCircuitFCRecvCurrentWndw':dlswCircuitFCRecvCurrentWndw,'dlswCircuitFCLargestRecvGranted':dlswCircuitFCLargestRecvGranted,'dlswCircuitFCLargestSendGranted':dlswCircuitFCLargestSendGranted,'dlswSdlc':dlswSdlc,'dlswSdlcPortTable':dlswSdlcPortTable,'dlswSdlcPortEntry':dlswSdlcPortEntry,'dlswSdlcPortSerialName':dlswSdlcPortSerialName,'dlswSdlcPortEncap':dlswSdlcPortEncap,'dlswSdlcPortRole':dlswSdlcPortRole,'dlswSdlcPortVmac':dlswSdlcPortVmac,'dlswSdlcPortHoldq':dlswSdlcPortHoldq,'dlswSdlcPortK':dlswSdlcPortK,'dlswSdlcPortModule':dlswSdlcPortModule,'dlswSdlcPortN1':dlswSdlcPortN1,'dlswSdlcPortN2':dlswSdlcPortN2,'dlswSdlcPortPollPauseTimer':dlswSdlcPortPollPauseTimer,'dlswSdlcPortSimultaneousEnable':dlswSdlcPortSimultaneousEnable,'dlswSdlcPortT1':dlswSdlcPortT1,'dlswSdlcPortT2':dlswSdlcPortT2,'dlswSdlcPortNrziEncoding':dlswSdlcPortNrziEncoding,'dlswSdlcPortIdleMarkEnable':dlswSdlcPortIdleMarkEnable,'dlswSdlcLsTable':dlswSdlcLsTable,'dlswSdlcLsEntry':dlswSdlcLsEntry,_a:dlswSdlcLsAddress,'dlswSdlcLsLocalId':dlswSdlcLsLocalId,'dlswSdlcLsRemoteMac':dlswSdlcLsRemoteMac,'dlswSdlcLsSsap':dlswSdlcLsSsap,'dlswSdlcLsDsap':dlswSdlcLsDsap,'dlswSdlcLsStatus':dlswSdlcLsStatus,'dlswLlc2':dlswLlc2,'dlswLlc2PortTable':dlswLlc2PortTable,'dlswLlc2PortEntry':dlswLlc2PortEntry,'dlswLLC2PortAckDelayTime':dlswLLC2PortAckDelayTime,'dlswLLC2PortAckMax':dlswLLC2PortAckMax,'dlswLLC2PortLocalWnd':dlswLLC2PortLocalWnd,'dlswLLC2PortModulus':dlswLLC2PortModulus,'dlswLLC2PortN2':dlswLLC2PortN2,'dlswLLC2PortT1':dlswLLC2PortT1,'dlswLLC2PortTbusyTime':dlswLLC2PortTbusyTime,'dlswLLC2PortTpfTime':dlswLLC2PortTpfTime,'dlswLLC2PortTrejTime':dlswLLC2PortTrejTime,'dlswLLC2PortTxqMax':dlswLLC2PortTxqMax,'dlswTraps':dlswTraps,'dlswTrapsV2':dlswTrapsV2,'dlswTrapTConnPartnerReject':dlswTrapTConnPartnerReject,'dlswTrapTConnChangeState':dlswTrapTConnChangeState,'dlswTrapCircuitChangeState':dlswTrapCircuitChangeState})