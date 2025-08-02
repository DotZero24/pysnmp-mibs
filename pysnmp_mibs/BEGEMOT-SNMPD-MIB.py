_a='begemotSnmpdTransInetProto'
_Z='begemotSnmpdTransInetPort'
_Y='begemotSnmpdTransInetAddress'
_X='begemotSnmpdTransInetAddressType'
_W='begemotSnmpdTransportName'
_V='begemotSnmpdLocalPortPath'
_U='begemotSnmpdModuleSection'
_T='begemotSnmpdCommunityIndex'
_S='begemotSnmpdCommunityModule'
_R='invalid'
_Q='begemotSnmpdPortPort'
_P='begemotSnmpdPortAddress'
_O='begemotTrapSinkPort'
_N='begemotTrapSinkAddr'
_M='InetPortNumber'
_L='InetAddress'
_K='TruthValue'
_J='OctetString'
_I='deprecated'
_H='Unsigned32'
_G='read-create'
_F='read-write'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='BEGEMOT-SNMPD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,'InetAddressType',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
begemotSnmpd=ModuleIdentity((1,3,6,1,4,1,12325,1,1))
if mibBuilder.loadTexts:begemotSnmpd.setRevisions(('2018-08-08 00:00',))
class SectionName(TextualConvention,OctetString):status=_A;displayHint='14a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
class BegemotSnmpdTransportProto(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('udp',1))
_BegemotSnmpdObjects_ObjectIdentity=ObjectIdentity
begemotSnmpdObjects=_BegemotSnmpdObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1))
_BegemotSnmpdConfig_ObjectIdentity=ObjectIdentity
begemotSnmpdConfig=_BegemotSnmpdConfig_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,1))
class _BegemotSnmpdTransmitBuffer_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,65535))
_BegemotSnmpdTransmitBuffer_Type.__name__=_D
_BegemotSnmpdTransmitBuffer_Object=MibScalar
begemotSnmpdTransmitBuffer=_BegemotSnmpdTransmitBuffer_Object((1,3,6,1,4,1,12325,1,1,1,1,1),_BegemotSnmpdTransmitBuffer_Type())
begemotSnmpdTransmitBuffer.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdTransmitBuffer.setStatus(_A)
class _BegemotSnmpdReceiveBuffer_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,65535))
_BegemotSnmpdReceiveBuffer_Type.__name__=_D
_BegemotSnmpdReceiveBuffer_Object=MibScalar
begemotSnmpdReceiveBuffer=_BegemotSnmpdReceiveBuffer_Object((1,3,6,1,4,1,12325,1,1,1,1,2),_BegemotSnmpdReceiveBuffer_Type())
begemotSnmpdReceiveBuffer.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdReceiveBuffer.setStatus(_A)
class _BegemotSnmpdCommunityDisable_Type(TruthValue):defaultValue=2
_BegemotSnmpdCommunityDisable_Type.__name__=_K
_BegemotSnmpdCommunityDisable_Object=MibScalar
begemotSnmpdCommunityDisable=_BegemotSnmpdCommunityDisable_Object((1,3,6,1,4,1,12325,1,1,1,1,3),_BegemotSnmpdCommunityDisable_Type())
begemotSnmpdCommunityDisable.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdCommunityDisable.setStatus(_A)
_BegemotSnmpdTrap1Addr_Type=IpAddress
_BegemotSnmpdTrap1Addr_Object=MibScalar
begemotSnmpdTrap1Addr=_BegemotSnmpdTrap1Addr_Object((1,3,6,1,4,1,12325,1,1,1,1,4),_BegemotSnmpdTrap1Addr_Type())
begemotSnmpdTrap1Addr.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdTrap1Addr.setStatus(_A)
class _BegemotSnmpdVersionEnable_Type(Unsigned32):defaultValue=3
_BegemotSnmpdVersionEnable_Type.__name__=_H
_BegemotSnmpdVersionEnable_Object=MibScalar
begemotSnmpdVersionEnable=_BegemotSnmpdVersionEnable_Object((1,3,6,1,4,1,12325,1,1,1,1,5),_BegemotSnmpdVersionEnable_Type())
begemotSnmpdVersionEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdVersionEnable.setStatus(_A)
_BegemotTrapSinkTable_Object=MibTable
begemotTrapSinkTable=_BegemotTrapSinkTable_Object((1,3,6,1,4,1,12325,1,1,1,2))
if mibBuilder.loadTexts:begemotTrapSinkTable.setStatus(_A)
_BegemotTrapSinkEntry_Object=MibTableRow
begemotTrapSinkEntry=_BegemotTrapSinkEntry_Object((1,3,6,1,4,1,12325,1,1,1,2,1))
begemotTrapSinkEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:begemotTrapSinkEntry.setStatus(_A)
_BegemotTrapSinkAddr_Type=IpAddress
_BegemotTrapSinkAddr_Object=MibTableColumn
begemotTrapSinkAddr=_BegemotTrapSinkAddr_Object((1,3,6,1,4,1,12325,1,1,1,2,1,1),_BegemotTrapSinkAddr_Type())
begemotTrapSinkAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotTrapSinkAddr.setStatus(_A)
class _BegemotTrapSinkPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotTrapSinkPort_Type.__name__=_D
_BegemotTrapSinkPort_Object=MibTableColumn
begemotTrapSinkPort=_BegemotTrapSinkPort_Object((1,3,6,1,4,1,12325,1,1,1,2,1,2),_BegemotTrapSinkPort_Type())
begemotTrapSinkPort.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotTrapSinkPort.setStatus(_A)
_BegemotTrapSinkStatus_Type=RowStatus
_BegemotTrapSinkStatus_Object=MibTableColumn
begemotTrapSinkStatus=_BegemotTrapSinkStatus_Object((1,3,6,1,4,1,12325,1,1,1,2,1,3),_BegemotTrapSinkStatus_Type())
begemotTrapSinkStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotTrapSinkStatus.setStatus(_A)
_BegemotSnmpdPortTable_Object=MibTable
begemotSnmpdPortTable=_BegemotSnmpdPortTable_Object((1,3,6,1,4,1,12325,1,1,1,4))
if mibBuilder.loadTexts:begemotSnmpdPortTable.setStatus(_I)
_BegemotSnmpdPortEntry_Object=MibTableRow
begemotSnmpdPortEntry=_BegemotSnmpdPortEntry_Object((1,3,6,1,4,1,12325,1,1,1,4,1))
begemotSnmpdPortEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:begemotSnmpdPortEntry.setStatus(_I)
_BegemotSnmpdPortAddress_Type=IpAddress
_BegemotSnmpdPortAddress_Object=MibTableColumn
begemotSnmpdPortAddress=_BegemotSnmpdPortAddress_Object((1,3,6,1,4,1,12325,1,1,1,4,1,1),_BegemotSnmpdPortAddress_Type())
begemotSnmpdPortAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdPortAddress.setStatus(_I)
class _BegemotSnmpdPortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotSnmpdPortPort_Type.__name__=_D
_BegemotSnmpdPortPort_Object=MibTableColumn
begemotSnmpdPortPort=_BegemotSnmpdPortPort_Object((1,3,6,1,4,1,12325,1,1,1,4,1,2),_BegemotSnmpdPortPort_Type())
begemotSnmpdPortPort.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdPortPort.setStatus(_I)
class _BegemotSnmpdPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_R,2)))
_BegemotSnmpdPortStatus_Type.__name__=_D
_BegemotSnmpdPortStatus_Object=MibTableColumn
begemotSnmpdPortStatus=_BegemotSnmpdPortStatus_Object((1,3,6,1,4,1,12325,1,1,1,4,1,3),_BegemotSnmpdPortStatus_Type())
begemotSnmpdPortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotSnmpdPortStatus.setStatus(_I)
_BegemotSnmpdCommunityTable_Object=MibTable
begemotSnmpdCommunityTable=_BegemotSnmpdCommunityTable_Object((1,3,6,1,4,1,12325,1,1,1,5))
if mibBuilder.loadTexts:begemotSnmpdCommunityTable.setStatus(_A)
_BegemotSnmpdCommunityEntry_Object=MibTableRow
begemotSnmpdCommunityEntry=_BegemotSnmpdCommunityEntry_Object((1,3,6,1,4,1,12325,1,1,1,5,1))
begemotSnmpdCommunityEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:begemotSnmpdCommunityEntry.setStatus(_A)
_BegemotSnmpdCommunityModule_Type=SectionName
_BegemotSnmpdCommunityModule_Object=MibTableColumn
begemotSnmpdCommunityModule=_BegemotSnmpdCommunityModule_Object((1,3,6,1,4,1,12325,1,1,1,5,1,1),_BegemotSnmpdCommunityModule_Type())
begemotSnmpdCommunityModule.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdCommunityModule.setStatus(_A)
class _BegemotSnmpdCommunityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BegemotSnmpdCommunityIndex_Type.__name__=_H
_BegemotSnmpdCommunityIndex_Object=MibTableColumn
begemotSnmpdCommunityIndex=_BegemotSnmpdCommunityIndex_Object((1,3,6,1,4,1,12325,1,1,1,5,1,2),_BegemotSnmpdCommunityIndex_Type())
begemotSnmpdCommunityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdCommunityIndex.setStatus(_A)
_BegemotSnmpdCommunityString_Type=OctetString
_BegemotSnmpdCommunityString_Object=MibTableColumn
begemotSnmpdCommunityString=_BegemotSnmpdCommunityString_Object((1,3,6,1,4,1,12325,1,1,1,5,1,3),_BegemotSnmpdCommunityString_Type())
begemotSnmpdCommunityString.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdCommunityString.setStatus(_A)
_BegemotSnmpdCommunityDescr_Type=OctetString
_BegemotSnmpdCommunityDescr_Object=MibTableColumn
begemotSnmpdCommunityDescr=_BegemotSnmpdCommunityDescr_Object((1,3,6,1,4,1,12325,1,1,1,5,1,4),_BegemotSnmpdCommunityDescr_Type())
begemotSnmpdCommunityDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdCommunityDescr.setStatus(_A)
class _BegemotSnmpdCommunityPermission_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BegemotSnmpdCommunityPermission_Type.__name__=_H
_BegemotSnmpdCommunityPermission_Object=MibTableColumn
begemotSnmpdCommunityPermission=_BegemotSnmpdCommunityPermission_Object((1,3,6,1,4,1,12325,1,1,1,5,1,5),_BegemotSnmpdCommunityPermission_Type())
begemotSnmpdCommunityPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdCommunityPermission.setStatus(_A)
_BegemotSnmpdModuleTable_Object=MibTable
begemotSnmpdModuleTable=_BegemotSnmpdModuleTable_Object((1,3,6,1,4,1,12325,1,1,1,6))
if mibBuilder.loadTexts:begemotSnmpdModuleTable.setStatus(_A)
_BegemotSnmpdModuleEntry_Object=MibTableRow
begemotSnmpdModuleEntry=_BegemotSnmpdModuleEntry_Object((1,3,6,1,4,1,12325,1,1,1,6,1))
begemotSnmpdModuleEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:begemotSnmpdModuleEntry.setStatus(_A)
_BegemotSnmpdModuleSection_Type=SectionName
_BegemotSnmpdModuleSection_Object=MibTableColumn
begemotSnmpdModuleSection=_BegemotSnmpdModuleSection_Object((1,3,6,1,4,1,12325,1,1,1,6,1,1),_BegemotSnmpdModuleSection_Type())
begemotSnmpdModuleSection.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdModuleSection.setStatus(_A)
_BegemotSnmpdModulePath_Type=OctetString
_BegemotSnmpdModulePath_Object=MibTableColumn
begemotSnmpdModulePath=_BegemotSnmpdModulePath_Object((1,3,6,1,4,1,12325,1,1,1,6,1,2),_BegemotSnmpdModulePath_Type())
begemotSnmpdModulePath.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotSnmpdModulePath.setStatus(_A)
_BegemotSnmpdModuleComment_Type=OctetString
_BegemotSnmpdModuleComment_Object=MibTableColumn
begemotSnmpdModuleComment=_BegemotSnmpdModuleComment_Object((1,3,6,1,4,1,12325,1,1,1,6,1,3),_BegemotSnmpdModuleComment_Type())
begemotSnmpdModuleComment.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdModuleComment.setStatus(_A)
_BegemotSnmpdStats_ObjectIdentity=ObjectIdentity
begemotSnmpdStats=_BegemotSnmpdStats_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,7))
_BegemotSnmpdStatsNoRxBufs_Type=Counter32
_BegemotSnmpdStatsNoRxBufs_Object=MibScalar
begemotSnmpdStatsNoRxBufs=_BegemotSnmpdStatsNoRxBufs_Object((1,3,6,1,4,1,12325,1,1,1,7,1),_BegemotSnmpdStatsNoRxBufs_Type())
begemotSnmpdStatsNoRxBufs.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdStatsNoRxBufs.setStatus(_A)
_BegemotSnmpdStatsNoTxBufs_Type=Counter32
_BegemotSnmpdStatsNoTxBufs_Object=MibScalar
begemotSnmpdStatsNoTxBufs=_BegemotSnmpdStatsNoTxBufs_Object((1,3,6,1,4,1,12325,1,1,1,7,2),_BegemotSnmpdStatsNoTxBufs_Type())
begemotSnmpdStatsNoTxBufs.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdStatsNoTxBufs.setStatus(_A)
_BegemotSnmpdStatsInTooLongPkts_Type=Counter32
_BegemotSnmpdStatsInTooLongPkts_Object=MibScalar
begemotSnmpdStatsInTooLongPkts=_BegemotSnmpdStatsInTooLongPkts_Object((1,3,6,1,4,1,12325,1,1,1,7,3),_BegemotSnmpdStatsInTooLongPkts_Type())
begemotSnmpdStatsInTooLongPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdStatsInTooLongPkts.setStatus(_A)
_BegemotSnmpdStatsInBadPduTypes_Type=Counter32
_BegemotSnmpdStatsInBadPduTypes_Object=MibScalar
begemotSnmpdStatsInBadPduTypes=_BegemotSnmpdStatsInBadPduTypes_Object((1,3,6,1,4,1,12325,1,1,1,7,4),_BegemotSnmpdStatsInBadPduTypes_Type())
begemotSnmpdStatsInBadPduTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdStatsInBadPduTypes.setStatus(_A)
_BegemotSnmpdDebug_ObjectIdentity=ObjectIdentity
begemotSnmpdDebug=_BegemotSnmpdDebug_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,8))
class _BegemotSnmpdDebugDumpPdus_Type(TruthValue):defaultValue=2
_BegemotSnmpdDebugDumpPdus_Type.__name__=_K
_BegemotSnmpdDebugDumpPdus_Object=MibScalar
begemotSnmpdDebugDumpPdus=_BegemotSnmpdDebugDumpPdus_Object((1,3,6,1,4,1,12325,1,1,1,8,1),_BegemotSnmpdDebugDumpPdus_Type())
begemotSnmpdDebugDumpPdus.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdDebugDumpPdus.setStatus(_A)
class _BegemotSnmpdDebugSnmpTrace_Type(Unsigned32):defaultValue=0
_BegemotSnmpdDebugSnmpTrace_Type.__name__=_H
_BegemotSnmpdDebugSnmpTrace_Object=MibScalar
begemotSnmpdDebugSnmpTrace=_BegemotSnmpdDebugSnmpTrace_Object((1,3,6,1,4,1,12325,1,1,1,8,2),_BegemotSnmpdDebugSnmpTrace_Type())
begemotSnmpdDebugSnmpTrace.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdDebugSnmpTrace.setStatus(_A)
class _BegemotSnmpdDebugSyslogPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_BegemotSnmpdDebugSyslogPri_Type.__name__=_D
_BegemotSnmpdDebugSyslogPri_Object=MibScalar
begemotSnmpdDebugSyslogPri=_BegemotSnmpdDebugSyslogPri_Object((1,3,6,1,4,1,12325,1,1,1,8,3),_BegemotSnmpdDebugSyslogPri_Type())
begemotSnmpdDebugSyslogPri.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotSnmpdDebugSyslogPri.setStatus(_A)
_BegemotSnmpdLocalPortTable_Object=MibTable
begemotSnmpdLocalPortTable=_BegemotSnmpdLocalPortTable_Object((1,3,6,1,4,1,12325,1,1,1,9))
if mibBuilder.loadTexts:begemotSnmpdLocalPortTable.setStatus(_A)
_BegemotSnmpdLocalPortEntry_Object=MibTableRow
begemotSnmpdLocalPortEntry=_BegemotSnmpdLocalPortEntry_Object((1,3,6,1,4,1,12325,1,1,1,9,1))
begemotSnmpdLocalPortEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:begemotSnmpdLocalPortEntry.setStatus(_A)
class _BegemotSnmpdLocalPortPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,104))
_BegemotSnmpdLocalPortPath_Type.__name__=_J
_BegemotSnmpdLocalPortPath_Object=MibTableColumn
begemotSnmpdLocalPortPath=_BegemotSnmpdLocalPortPath_Object((1,3,6,1,4,1,12325,1,1,1,9,1,1),_BegemotSnmpdLocalPortPath_Type())
begemotSnmpdLocalPortPath.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdLocalPortPath.setStatus(_A)
class _BegemotSnmpdLocalPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_R,2)))
_BegemotSnmpdLocalPortStatus_Type.__name__=_D
_BegemotSnmpdLocalPortStatus_Object=MibTableColumn
begemotSnmpdLocalPortStatus=_BegemotSnmpdLocalPortStatus_Object((1,3,6,1,4,1,12325,1,1,1,9,1,2),_BegemotSnmpdLocalPortStatus_Type())
begemotSnmpdLocalPortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotSnmpdLocalPortStatus.setStatus(_A)
class _BegemotSnmpdLocalPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dgram-unpriv',1),('dgram-priv',2),('stream-unpriv',3),('stream-priv',4)))
_BegemotSnmpdLocalPortType_Type.__name__=_D
_BegemotSnmpdLocalPortType_Object=MibTableColumn
begemotSnmpdLocalPortType=_BegemotSnmpdLocalPortType_Object((1,3,6,1,4,1,12325,1,1,1,9,1,3),_BegemotSnmpdLocalPortType_Type())
begemotSnmpdLocalPortType.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotSnmpdLocalPortType.setStatus(_A)
_BegemotSnmpdTransportMappings_ObjectIdentity=ObjectIdentity
begemotSnmpdTransportMappings=_BegemotSnmpdTransportMappings_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,10))
_BegemotSnmpdTransportTable_Object=MibTable
begemotSnmpdTransportTable=_BegemotSnmpdTransportTable_Object((1,3,6,1,4,1,12325,1,1,1,10,1))
if mibBuilder.loadTexts:begemotSnmpdTransportTable.setStatus(_A)
_BegemotSnmpdTransportEntry_Object=MibTableRow
begemotSnmpdTransportEntry=_BegemotSnmpdTransportEntry_Object((1,3,6,1,4,1,12325,1,1,1,10,1,1))
begemotSnmpdTransportEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:begemotSnmpdTransportEntry.setStatus(_A)
class _BegemotSnmpdTransportName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_BegemotSnmpdTransportName_Type.__name__=_J
_BegemotSnmpdTransportName_Object=MibTableColumn
begemotSnmpdTransportName=_BegemotSnmpdTransportName_Object((1,3,6,1,4,1,12325,1,1,1,10,1,1,1),_BegemotSnmpdTransportName_Type())
begemotSnmpdTransportName.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdTransportName.setStatus(_A)
_BegemotSnmpdTransportStatus_Type=RowStatus
_BegemotSnmpdTransportStatus_Object=MibTableColumn
begemotSnmpdTransportStatus=_BegemotSnmpdTransportStatus_Object((1,3,6,1,4,1,12325,1,1,1,10,1,1,2),_BegemotSnmpdTransportStatus_Type())
begemotSnmpdTransportStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdTransportStatus.setStatus(_A)
_BegemotSnmpdTransportOid_Type=ObjectIdentifier
_BegemotSnmpdTransportOid_Object=MibTableColumn
begemotSnmpdTransportOid=_BegemotSnmpdTransportOid_Object((1,3,6,1,4,1,12325,1,1,1,10,1,1,3),_BegemotSnmpdTransportOid_Type())
begemotSnmpdTransportOid.setMaxAccess(_E)
if mibBuilder.loadTexts:begemotSnmpdTransportOid.setStatus(_A)
_BegemotSnmpdTransUdp_ObjectIdentity=ObjectIdentity
begemotSnmpdTransUdp=_BegemotSnmpdTransUdp_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,10,2))
_BegemotSnmpdTransLsock_ObjectIdentity=ObjectIdentity
begemotSnmpdTransLsock=_BegemotSnmpdTransLsock_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,10,3))
_BegemotSnmpdTransInet_ObjectIdentity=ObjectIdentity
begemotSnmpdTransInet=_BegemotSnmpdTransInet_ObjectIdentity((1,3,6,1,4,1,12325,1,1,1,10,4))
_BegemotSnmpdTransInetTable_Object=MibTable
begemotSnmpdTransInetTable=_BegemotSnmpdTransInetTable_Object((1,3,6,1,4,1,12325,1,1,1,11))
if mibBuilder.loadTexts:begemotSnmpdTransInetTable.setStatus(_A)
_BegemotSnmpdTransInetEntry_Object=MibTableRow
begemotSnmpdTransInetEntry=_BegemotSnmpdTransInetEntry_Object((1,3,6,1,4,1,12325,1,1,1,11,1))
begemotSnmpdTransInetEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:begemotSnmpdTransInetEntry.setStatus(_A)
_BegemotSnmpdTransInetAddressType_Type=InetAddressType
_BegemotSnmpdTransInetAddressType_Object=MibTableColumn
begemotSnmpdTransInetAddressType=_BegemotSnmpdTransInetAddressType_Object((1,3,6,1,4,1,12325,1,1,1,11,1,1),_BegemotSnmpdTransInetAddressType_Type())
begemotSnmpdTransInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdTransInetAddressType.setStatus(_A)
class _BegemotSnmpdTransInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BegemotSnmpdTransInetAddress_Type.__name__=_L
_BegemotSnmpdTransInetAddress_Object=MibTableColumn
begemotSnmpdTransInetAddress=_BegemotSnmpdTransInetAddress_Object((1,3,6,1,4,1,12325,1,1,1,11,1,2),_BegemotSnmpdTransInetAddress_Type())
begemotSnmpdTransInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdTransInetAddress.setStatus(_A)
class _BegemotSnmpdTransInetPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotSnmpdTransInetPort_Type.__name__=_M
_BegemotSnmpdTransInetPort_Object=MibTableColumn
begemotSnmpdTransInetPort=_BegemotSnmpdTransInetPort_Object((1,3,6,1,4,1,12325,1,1,1,11,1,3),_BegemotSnmpdTransInetPort_Type())
begemotSnmpdTransInetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdTransInetPort.setStatus(_A)
_BegemotSnmpdTransInetProto_Type=BegemotSnmpdTransportProto
_BegemotSnmpdTransInetProto_Object=MibTableColumn
begemotSnmpdTransInetProto=_BegemotSnmpdTransInetProto_Object((1,3,6,1,4,1,12325,1,1,1,11,1,4),_BegemotSnmpdTransInetProto_Type())
begemotSnmpdTransInetProto.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotSnmpdTransInetProto.setStatus(_A)
_BegemotSnmpdTransInetStatus_Type=RowStatus
_BegemotSnmpdTransInetStatus_Object=MibTableColumn
begemotSnmpdTransInetStatus=_BegemotSnmpdTransInetStatus_Object((1,3,6,1,4,1,12325,1,1,1,11,1,5),_BegemotSnmpdTransInetStatus_Type())
begemotSnmpdTransInetStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotSnmpdTransInetStatus.setStatus(_A)
_BegemotSnmpdDefs_ObjectIdentity=ObjectIdentity
begemotSnmpdDefs=_BegemotSnmpdDefs_ObjectIdentity((1,3,6,1,4,1,12325,1,1,2))
_BegemotSnmpdAgent_ObjectIdentity=ObjectIdentity
begemotSnmpdAgent=_BegemotSnmpdAgent_ObjectIdentity((1,3,6,1,4,1,12325,1,1,2,1))
_BegemotSnmpdAgentFreeBSD_ObjectIdentity=ObjectIdentity
begemotSnmpdAgentFreeBSD=_BegemotSnmpdAgentFreeBSD_ObjectIdentity((1,3,6,1,4,1,12325,1,1,2,1,1))
if mibBuilder.loadTexts:begemotSnmpdAgentFreeBSD.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SectionName':SectionName,'BegemotSnmpdTransportProto':BegemotSnmpdTransportProto,'begemotSnmpd':begemotSnmpd,'begemotSnmpdObjects':begemotSnmpdObjects,'begemotSnmpdConfig':begemotSnmpdConfig,'begemotSnmpdTransmitBuffer':begemotSnmpdTransmitBuffer,'begemotSnmpdReceiveBuffer':begemotSnmpdReceiveBuffer,'begemotSnmpdCommunityDisable':begemotSnmpdCommunityDisable,'begemotSnmpdTrap1Addr':begemotSnmpdTrap1Addr,'begemotSnmpdVersionEnable':begemotSnmpdVersionEnable,'begemotTrapSinkTable':begemotTrapSinkTable,'begemotTrapSinkEntry':begemotTrapSinkEntry,_N:begemotTrapSinkAddr,_O:begemotTrapSinkPort,'begemotTrapSinkStatus':begemotTrapSinkStatus,'begemotSnmpdPortTable':begemotSnmpdPortTable,'begemotSnmpdPortEntry':begemotSnmpdPortEntry,_P:begemotSnmpdPortAddress,_Q:begemotSnmpdPortPort,'begemotSnmpdPortStatus':begemotSnmpdPortStatus,'begemotSnmpdCommunityTable':begemotSnmpdCommunityTable,'begemotSnmpdCommunityEntry':begemotSnmpdCommunityEntry,_S:begemotSnmpdCommunityModule,_T:begemotSnmpdCommunityIndex,'begemotSnmpdCommunityString':begemotSnmpdCommunityString,'begemotSnmpdCommunityDescr':begemotSnmpdCommunityDescr,'begemotSnmpdCommunityPermission':begemotSnmpdCommunityPermission,'begemotSnmpdModuleTable':begemotSnmpdModuleTable,'begemotSnmpdModuleEntry':begemotSnmpdModuleEntry,_U:begemotSnmpdModuleSection,'begemotSnmpdModulePath':begemotSnmpdModulePath,'begemotSnmpdModuleComment':begemotSnmpdModuleComment,'begemotSnmpdStats':begemotSnmpdStats,'begemotSnmpdStatsNoRxBufs':begemotSnmpdStatsNoRxBufs,'begemotSnmpdStatsNoTxBufs':begemotSnmpdStatsNoTxBufs,'begemotSnmpdStatsInTooLongPkts':begemotSnmpdStatsInTooLongPkts,'begemotSnmpdStatsInBadPduTypes':begemotSnmpdStatsInBadPduTypes,'begemotSnmpdDebug':begemotSnmpdDebug,'begemotSnmpdDebugDumpPdus':begemotSnmpdDebugDumpPdus,'begemotSnmpdDebugSnmpTrace':begemotSnmpdDebugSnmpTrace,'begemotSnmpdDebugSyslogPri':begemotSnmpdDebugSyslogPri,'begemotSnmpdLocalPortTable':begemotSnmpdLocalPortTable,'begemotSnmpdLocalPortEntry':begemotSnmpdLocalPortEntry,_V:begemotSnmpdLocalPortPath,'begemotSnmpdLocalPortStatus':begemotSnmpdLocalPortStatus,'begemotSnmpdLocalPortType':begemotSnmpdLocalPortType,'begemotSnmpdTransportMappings':begemotSnmpdTransportMappings,'begemotSnmpdTransportTable':begemotSnmpdTransportTable,'begemotSnmpdTransportEntry':begemotSnmpdTransportEntry,_W:begemotSnmpdTransportName,'begemotSnmpdTransportStatus':begemotSnmpdTransportStatus,'begemotSnmpdTransportOid':begemotSnmpdTransportOid,'begemotSnmpdTransUdp':begemotSnmpdTransUdp,'begemotSnmpdTransLsock':begemotSnmpdTransLsock,'begemotSnmpdTransInet':begemotSnmpdTransInet,'begemotSnmpdTransInetTable':begemotSnmpdTransInetTable,'begemotSnmpdTransInetEntry':begemotSnmpdTransInetEntry,_X:begemotSnmpdTransInetAddressType,_Y:begemotSnmpdTransInetAddress,_Z:begemotSnmpdTransInetPort,_a:begemotSnmpdTransInetProto,'begemotSnmpdTransInetStatus':begemotSnmpdTransInetStatus,'begemotSnmpdDefs':begemotSnmpdDefs,'begemotSnmpdAgent':begemotSnmpdAgent,'begemotSnmpdAgentFreeBSD':begemotSnmpdAgentFreeBSD})