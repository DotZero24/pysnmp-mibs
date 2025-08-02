_AN='portNotificationVarsGroup'
_AM='portMonitoringGroup'
_AL='portMirroringGroup'
_AK='monitorFileWritten'
_AJ='mirrorUnlikeNi'
_AI='mirrorConfigError'
_AH='alasFlowFsDeleteEntry'
_AG='alasFlowCpDeleteEntry'
_AF='mirrorTaggedVLAN'
_AE='alasFlowAgentConfigType'
_AD='alasFlowAgentAddressType'
_AC='alasFlowAgentAddress'
_AB='mirMonSession'
_AA='monitorSrcRowStatus'
_A9='monitorSrcDirection'
_A8='monitorSrcStatus'
_A7='monitorCaptureType'
_A6='monitorRowStatus'
_A5='monitorTimeout'
_A4='monitorDirection'
_A3='monitorFileOverWrite'
_A2='monitorStatus'
_A1='monitorTrafficType'
_A0='monitorScreenLine'
_z='monitorScreenStatus'
_y='monitorFileStatus'
_x='monitorIfindex'
_w='mirrorDstRowStatus'
_v='mirrorDstAdminStatus'
_u='mirrorDstOperStatus'
_t='mirrorSrcOperStatus'
_s='mirrorSrcRowStatus'
_r='mirrorSrcDirection'
_q='mirrorSrcStatus'
_p='alasFlowCpEntry'
_o='alasFlowFsEntry'
_n='delete'
_m='notInService'
_l='active'
_k='monitorSrcIfindex'
_j='not-accessible'
_i='mirrorDstMirroringIf'
_h='enable'
_g='disable'
_f='SnmpAdminString'
_e='InterfaceIndex'
_d='mirMonError'
_c='monitorFileSize'
_b='monitorFileName'
_a='mirrorSessOperStatus'
_Z='mirrorDirection'
_Y='mirrorRowStatus'
_X='mirrorUnblockedVLAN'
_W='mirrorStatus'
_V='mirrorMirroringIfindex'
_U='mirrorMirroredIfindex'
_T='mirrorSrcMirroredIf'
_S='mirMonErrorNi'
_R='mirroringPort'
_Q='mirroringSlot'
_P='monitorSessionNumber'
_O='bidirectional'
_N='outport'
_M='inport'
_L='mirmonPrimaryPort'
_K='mirmonPrimarySlot'
_J='read-write'
_I='deprecated'
_H='mirrorSessionNumber'
_G='on'
_F='off'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-PORT-MIRRORING-MONITORING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1PortMirroringMonitoring,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1PortMirroringMonitoring')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_e)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
sFlowCpEntry,sFlowFsEntry=mibBuilder.importSymbols('SFLOW-MIB','sFlowCpEntry','sFlowFsEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_f)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1PortMirrorMonitoringMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1))
if mibBuilder.loadTexts:alcatelIND1PortMirrorMonitoringMIB.setRevisions(('2007-04-03 00:00',))
class MirMonErrorIds(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('wrongSession',2),('hwQError',3),('swQError',4)))
_AlcatelIND1PortMirMonMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1PortMirMonMIBNotifications=_AlcatelIND1PortMirMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,0))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBNotifications.setStatus(_B)
_AlcatelIND1PortMirMonMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PortMirMonMIBObjects=_AlcatelIND1PortMirMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,1))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBObjects.setStatus(_B)
_MirmonMirroring_ObjectIdentity=ObjectIdentity
mirmonMirroring=_MirmonMirroring_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1))
_MirrorTable_Object=MibTable
mirrorTable=_MirrorTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1))
if mibBuilder.loadTexts:mirrorTable.setStatus(_B)
_MirrorEntry_Object=MibTableRow
mirrorEntry=_MirrorEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1))
mirrorEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:mirrorEntry.setStatus(_B)
class _MirrorSessionNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MirrorSessionNumber_Type.__name__=_C
_MirrorSessionNumber_Object=MibTableColumn
mirrorSessionNumber=_MirrorSessionNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,1),_MirrorSessionNumber_Type())
mirrorSessionNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorSessionNumber.setStatus(_B)
_MirrorMirroredIfindex_Type=InterfaceIndex
_MirrorMirroredIfindex_Object=MibTableColumn
mirrorMirroredIfindex=_MirrorMirroredIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,2),_MirrorMirroredIfindex_Type())
mirrorMirroredIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorMirroredIfindex.setStatus(_I)
_MirrorMirroringIfindex_Type=InterfaceIndex
_MirrorMirroringIfindex_Object=MibTableColumn
mirrorMirroringIfindex=_MirrorMirroringIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,3),_MirrorMirroringIfindex_Type())
mirrorMirroringIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorMirroringIfindex.setStatus(_I)
class _MirrorStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MirrorStatus_Type.__name__=_C
_MirrorStatus_Object=MibTableColumn
mirrorStatus=_MirrorStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,4),_MirrorStatus_Type())
mirrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorStatus.setStatus(_B)
class _MirrorUnblockedVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MirrorUnblockedVLAN_Type.__name__=_C
_MirrorUnblockedVLAN_Object=MibTableColumn
mirrorUnblockedVLAN=_MirrorUnblockedVLAN_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,5),_MirrorUnblockedVLAN_Type())
mirrorUnblockedVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorUnblockedVLAN.setStatus(_B)
_MirrorRowStatus_Type=RowStatus
_MirrorRowStatus_Object=MibTableColumn
mirrorRowStatus=_MirrorRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,6),_MirrorRowStatus_Type())
mirrorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorRowStatus.setStatus(_B)
class _MirrorDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_MirrorDirection_Type.__name__=_C
_MirrorDirection_Object=MibTableColumn
mirrorDirection=_MirrorDirection_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,7),_MirrorDirection_Type())
mirrorDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorDirection.setStatus(_I)
class _MirrorSessOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MirrorSessOperStatus_Type.__name__=_C
_MirrorSessOperStatus_Object=MibTableColumn
mirrorSessOperStatus=_MirrorSessOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,8),_MirrorSessOperStatus_Type())
mirrorSessOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorSessOperStatus.setStatus(_B)
class _MirrorTaggedVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MirrorTaggedVLAN_Type.__name__=_C
_MirrorTaggedVLAN_Object=MibTableColumn
mirrorTaggedVLAN=_MirrorTaggedVLAN_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,1,1,9),_MirrorTaggedVLAN_Type())
mirrorTaggedVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorTaggedVLAN.setStatus(_B)
_MirrorSrcTable_Object=MibTable
mirrorSrcTable=_MirrorSrcTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2))
if mibBuilder.loadTexts:mirrorSrcTable.setStatus(_B)
_MirrorSrcEntry_Object=MibTableRow
mirrorSrcEntry=_MirrorSrcEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1))
mirrorSrcEntry.setIndexNames((0,_A,_H),(0,_A,_T))
if mibBuilder.loadTexts:mirrorSrcEntry.setStatus(_B)
_MirrorSrcMirroredIf_Type=InterfaceIndex
_MirrorSrcMirroredIf_Object=MibTableColumn
mirrorSrcMirroredIf=_MirrorSrcMirroredIf_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1,1),_MirrorSrcMirroredIf_Type())
mirrorSrcMirroredIf.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorSrcMirroredIf.setStatus(_B)
class _MirrorSrcStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_MirrorSrcStatus_Type.__name__=_C
_MirrorSrcStatus_Object=MibTableColumn
mirrorSrcStatus=_MirrorSrcStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1,2),_MirrorSrcStatus_Type())
mirrorSrcStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorSrcStatus.setStatus(_B)
class _MirrorSrcDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_MirrorSrcDirection_Type.__name__=_C
_MirrorSrcDirection_Object=MibTableColumn
mirrorSrcDirection=_MirrorSrcDirection_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1,3),_MirrorSrcDirection_Type())
mirrorSrcDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorSrcDirection.setStatus(_B)
_MirrorSrcRowStatus_Type=RowStatus
_MirrorSrcRowStatus_Object=MibTableColumn
mirrorSrcRowStatus=_MirrorSrcRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1,4),_MirrorSrcRowStatus_Type())
mirrorSrcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorSrcRowStatus.setStatus(_B)
class _MirrorSrcOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MirrorSrcOperStatus_Type.__name__=_C
_MirrorSrcOperStatus_Object=MibTableColumn
mirrorSrcOperStatus=_MirrorSrcOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,2,1,5),_MirrorSrcOperStatus_Type())
mirrorSrcOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorSrcOperStatus.setStatus(_B)
_MirrorDstTable_Object=MibTable
mirrorDstTable=_MirrorDstTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3))
if mibBuilder.loadTexts:mirrorDstTable.setStatus(_B)
_MirrorDstEntry_Object=MibTableRow
mirrorDstEntry=_MirrorDstEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3,1))
mirrorDstEntry.setIndexNames((0,_A,_H),(0,_A,_i))
if mibBuilder.loadTexts:mirrorDstEntry.setStatus(_B)
_MirrorDstMirroringIf_Type=InterfaceIndex
_MirrorDstMirroringIf_Object=MibTableColumn
mirrorDstMirroringIf=_MirrorDstMirroringIf_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3,1,1),_MirrorDstMirroringIf_Type())
mirrorDstMirroringIf.setMaxAccess(_j)
if mibBuilder.loadTexts:mirrorDstMirroringIf.setStatus(_B)
class _MirrorDstOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MirrorDstOperStatus_Type.__name__=_C
_MirrorDstOperStatus_Object=MibTableColumn
mirrorDstOperStatus=_MirrorDstOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3,1,2),_MirrorDstOperStatus_Type())
mirrorDstOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorDstOperStatus.setStatus(_B)
class _MirrorDstAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_g,2)))
_MirrorDstAdminStatus_Type.__name__=_C
_MirrorDstAdminStatus_Object=MibTableColumn
mirrorDstAdminStatus=_MirrorDstAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3,1,3),_MirrorDstAdminStatus_Type())
mirrorDstAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorDstAdminStatus.setStatus(_B)
_MirrorDstRowStatus_Type=RowStatus
_MirrorDstRowStatus_Object=MibTableColumn
mirrorDstRowStatus=_MirrorDstRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,1,3,1,4),_MirrorDstRowStatus_Type())
mirrorDstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorDstRowStatus.setStatus(_B)
_MirmonMonitoring_ObjectIdentity=ObjectIdentity
mirmonMonitoring=_MirmonMonitoring_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2))
_MonitorTable_Object=MibTable
monitorTable=_MonitorTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1))
if mibBuilder.loadTexts:monitorTable.setStatus(_B)
_MonitorEntry_Object=MibTableRow
monitorEntry=_MonitorEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1))
monitorEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:monitorEntry.setStatus(_B)
class _MonitorSessionNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MonitorSessionNumber_Type.__name__=_C
_MonitorSessionNumber_Object=MibTableColumn
monitorSessionNumber=_MonitorSessionNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,1),_MonitorSessionNumber_Type())
monitorSessionNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:monitorSessionNumber.setStatus(_B)
class _MonitorIfindex_Type(InterfaceIndex):defaultValue=1
_MonitorIfindex_Type.__name__=_e
_MonitorIfindex_Object=MibTableColumn
monitorIfindex=_MonitorIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,2),_MonitorIfindex_Type())
monitorIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorIfindex.setStatus(_I)
class _MonitorFileStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MonitorFileStatus_Type.__name__=_C
_MonitorFileStatus_Object=MibTableColumn
monitorFileStatus=_MonitorFileStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,3),_MonitorFileStatus_Type())
monitorFileStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFileStatus.setStatus(_B)
class _MonitorFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MonitorFileName_Type.__name__=_f
_MonitorFileName_Object=MibTableColumn
monitorFileName=_MonitorFileName_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,4),_MonitorFileName_Type())
monitorFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFileName.setStatus(_B)
class _MonitorFileSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_MonitorFileSize_Type.__name__=_C
_MonitorFileSize_Object=MibTableColumn
monitorFileSize=_MonitorFileSize_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,5),_MonitorFileSize_Type())
monitorFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFileSize.setStatus(_B)
class _MonitorScreenStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MonitorScreenStatus_Type.__name__=_C
_MonitorScreenStatus_Object=MibTableColumn
monitorScreenStatus=_MonitorScreenStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,6),_MonitorScreenStatus_Type())
monitorScreenStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorScreenStatus.setStatus(_B)
class _MonitorScreenLine_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MonitorScreenLine_Type.__name__=_C
_MonitorScreenLine_Object=MibTableColumn
monitorScreenLine=_MonitorScreenLine_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,7),_MonitorScreenLine_Type())
monitorScreenLine.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorScreenLine.setStatus(_B)
class _MonitorTrafficType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('all',1),('unicast',2),('multicast',3),('broadcast',4),('unimulti',5),('unibroad',6),('multibroad',7)))
_MonitorTrafficType_Type.__name__=_C
_MonitorTrafficType_Object=MibTableColumn
monitorTrafficType=_MonitorTrafficType_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,8),_MonitorTrafficType_Type())
monitorTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTrafficType.setStatus(_B)
class _MonitorStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('suspended',3)))
_MonitorStatus_Type.__name__=_C
_MonitorStatus_Object=MibTableColumn
monitorStatus=_MonitorStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,9),_MonitorStatus_Type())
monitorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorStatus.setStatus(_B)
class _MonitorFileOverWrite_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MonitorFileOverWrite_Type.__name__=_C
_MonitorFileOverWrite_Object=MibTableColumn
monitorFileOverWrite=_MonitorFileOverWrite_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,10),_MonitorFileOverWrite_Type())
monitorFileOverWrite.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorFileOverWrite.setStatus(_B)
class _MonitorDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_MonitorDirection_Type.__name__=_C
_MonitorDirection_Object=MibTableColumn
monitorDirection=_MonitorDirection_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,11),_MonitorDirection_Type())
monitorDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDirection.setStatus(_I)
class _MonitorTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MonitorTimeout_Type.__name__=_C
_MonitorTimeout_Object=MibTableColumn
monitorTimeout=_MonitorTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,12),_MonitorTimeout_Type())
monitorTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorTimeout.setStatus(_B)
_MonitorRowStatus_Type=RowStatus
_MonitorRowStatus_Object=MibTableColumn
monitorRowStatus=_MonitorRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,13),_MonitorRowStatus_Type())
monitorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorRowStatus.setStatus(_B)
class _MonitorCaptureType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('brief',1),('full',2)))
_MonitorCaptureType_Type.__name__=_C
_MonitorCaptureType_Object=MibTableColumn
monitorCaptureType=_MonitorCaptureType_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,1,1,14),_MonitorCaptureType_Type())
monitorCaptureType.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorCaptureType.setStatus(_B)
_MonitorSrcTable_Object=MibTable
monitorSrcTable=_MonitorSrcTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2))
if mibBuilder.loadTexts:monitorSrcTable.setStatus(_B)
_MonitorSrcEntry_Object=MibTableRow
monitorSrcEntry=_MonitorSrcEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2,1))
monitorSrcEntry.setIndexNames((0,_A,_P),(0,_A,_k))
if mibBuilder.loadTexts:monitorSrcEntry.setStatus(_B)
_MonitorSrcIfindex_Type=InterfaceIndex
_MonitorSrcIfindex_Object=MibTableColumn
monitorSrcIfindex=_MonitorSrcIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2,1,1),_MonitorSrcIfindex_Type())
monitorSrcIfindex.setMaxAccess(_j)
if mibBuilder.loadTexts:monitorSrcIfindex.setStatus(_B)
class _MonitorSrcStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MonitorSrcStatus_Type.__name__=_C
_MonitorSrcStatus_Object=MibTableColumn
monitorSrcStatus=_MonitorSrcStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2,1,2),_MonitorSrcStatus_Type())
monitorSrcStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSrcStatus.setStatus(_B)
class _MonitorSrcDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_MonitorSrcDirection_Type.__name__=_C
_MonitorSrcDirection_Object=MibTableColumn
monitorSrcDirection=_MonitorSrcDirection_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2,1,3),_MonitorSrcDirection_Type())
monitorSrcDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSrcDirection.setStatus(_B)
_MonitorSrcRowStatus_Type=RowStatus
_MonitorSrcRowStatus_Object=MibTableColumn
monitorSrcRowStatus=_MonitorSrcRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,2,2,1,4),_MonitorSrcRowStatus_Type())
monitorSrcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSrcRowStatus.setStatus(_B)
_MirmonNotificationVars_ObjectIdentity=ObjectIdentity
mirmonNotificationVars=_MirmonNotificationVars_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3))
class _MirmonPrimarySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MirmonPrimarySlot_Type.__name__=_C
_MirmonPrimarySlot_Object=MibScalar
mirmonPrimarySlot=_MirmonPrimarySlot_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,1),_MirmonPrimarySlot_Type())
mirmonPrimarySlot.setMaxAccess(_E)
if mibBuilder.loadTexts:mirmonPrimarySlot.setStatus(_B)
class _MirmonPrimaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_MirmonPrimaryPort_Type.__name__=_C
_MirmonPrimaryPort_Object=MibScalar
mirmonPrimaryPort=_MirmonPrimaryPort_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,2),_MirmonPrimaryPort_Type())
mirmonPrimaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:mirmonPrimaryPort.setStatus(_B)
class _MirroringSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MirroringSlot_Type.__name__=_C
_MirroringSlot_Object=MibScalar
mirroringSlot=_MirroringSlot_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,3),_MirroringSlot_Type())
mirroringSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:mirroringSlot.setStatus(_B)
class _MirroringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_MirroringPort_Type.__name__=_C
_MirroringPort_Object=MibScalar
mirroringPort=_MirroringPort_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,4),_MirroringPort_Type())
mirroringPort.setMaxAccess(_E)
if mibBuilder.loadTexts:mirroringPort.setStatus(_B)
class _MirMonSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MirMonSession_Type.__name__=_C
_MirMonSession_Object=MibScalar
mirMonSession=_MirMonSession_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,5),_MirMonSession_Type())
mirMonSession.setMaxAccess(_E)
if mibBuilder.loadTexts:mirMonSession.setStatus(_B)
_MirMonError_Type=MirMonErrorIds
_MirMonError_Object=MibScalar
mirMonError=_MirMonError_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,6),_MirMonError_Type())
mirMonError.setMaxAccess(_E)
if mibBuilder.loadTexts:mirMonError.setStatus(_B)
class _MirMonErrorNi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MirMonErrorNi_Type.__name__=_C
_MirMonErrorNi_Object=MibScalar
mirMonErrorNi=_MirMonErrorNi_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,3,7),_MirMonErrorNi_Type())
mirMonErrorNi.setMaxAccess(_E)
if mibBuilder.loadTexts:mirMonErrorNi.setStatus(_B)
_MirmonSFlowObjects_ObjectIdentity=ObjectIdentity
mirmonSFlowObjects=_MirmonSFlowObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4))
_AlasFlowFsTable_Object=MibTable
alasFlowFsTable=_AlasFlowFsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,1))
if mibBuilder.loadTexts:alasFlowFsTable.setStatus(_B)
_AlasFlowFsEntry_Object=MibTableRow
alasFlowFsEntry=_AlasFlowFsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,1,1))
if mibBuilder.loadTexts:alasFlowFsEntry.setStatus(_B)
class _AlasFlowFsDeleteEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,6)))
_AlasFlowFsDeleteEntry_Type.__name__=_C
_AlasFlowFsDeleteEntry_Object=MibTableColumn
alasFlowFsDeleteEntry=_AlasFlowFsDeleteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,1,1,1),_AlasFlowFsDeleteEntry_Type())
alasFlowFsDeleteEntry.setMaxAccess(_J)
if mibBuilder.loadTexts:alasFlowFsDeleteEntry.setStatus(_B)
_AlasFlowCpTable_Object=MibTable
alasFlowCpTable=_AlasFlowCpTable_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,2))
if mibBuilder.loadTexts:alasFlowCpTable.setStatus(_B)
_AlasFlowCpEntry_Object=MibTableRow
alasFlowCpEntry=_AlasFlowCpEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,2,1))
if mibBuilder.loadTexts:alasFlowCpEntry.setStatus(_B)
class _AlasFlowCpDeleteEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,6)))
_AlasFlowCpDeleteEntry_Type.__name__=_C
_AlasFlowCpDeleteEntry_Object=MibTableColumn
alasFlowCpDeleteEntry=_AlasFlowCpDeleteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,2,1,1),_AlasFlowCpDeleteEntry_Type())
alasFlowCpDeleteEntry.setMaxAccess(_J)
if mibBuilder.loadTexts:alasFlowCpDeleteEntry.setStatus(_B)
class _AlasFlowAgentConfigType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('user',2)))
_AlasFlowAgentConfigType_Type.__name__=_C
_AlasFlowAgentConfigType_Object=MibScalar
alasFlowAgentConfigType=_AlasFlowAgentConfigType_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,3),_AlasFlowAgentConfigType_Type())
alasFlowAgentConfigType.setMaxAccess(_J)
if mibBuilder.loadTexts:alasFlowAgentConfigType.setStatus(_B)
_AlasFlowAgentAddressType_Type=InetAddressType
_AlasFlowAgentAddressType_Object=MibScalar
alasFlowAgentAddressType=_AlasFlowAgentAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,4),_AlasFlowAgentAddressType_Type())
alasFlowAgentAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:alasFlowAgentAddressType.setStatus(_B)
_AlasFlowAgentAddress_Type=InetAddress
_AlasFlowAgentAddress_Object=MibScalar
alasFlowAgentAddress=_AlasFlowAgentAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,19,1,1,4,5),_AlasFlowAgentAddress_Type())
alasFlowAgentAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:alasFlowAgentAddress.setStatus(_B)
_AlcatelIND1PortMirMonMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PortMirMonMIBConformance=_AlcatelIND1PortMirMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,2))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBConformance.setStatus(_B)
_AlcatelIND1PortMirMonMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PortMirMonMIBGroups=_AlcatelIND1PortMirMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBGroups.setStatus(_B)
_AlcatelIND1PortMirMonMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PortMirMonMIBCompliances=_AlcatelIND1PortMirMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,2))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBCompliances.setStatus(_B)
sFlowFsEntry.registerAugmentions((_A,_o))
alasFlowFsEntry.setIndexNames(*sFlowFsEntry.getIndexNames())
sFlowCpEntry.registerAugmentions((_A,_p))
alasFlowCpEntry.setIndexNames(*sFlowCpEntry.getIndexNames())
portMirroringGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,1))
portMirroringGroup.setObjects(*((_A,_H),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_T),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:portMirroringGroup.setStatus(_B)
portMonitoringGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,2))
portMonitoringGroup.setObjects(*((_A,_P),(_A,_x),(_A,_y),(_A,_b),(_A,_c),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:portMonitoringGroup.setStatus(_B)
portNotificationVarsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,3))
portNotificationVarsGroup.setObjects(*((_A,_K),(_A,_L),(_A,_Q),(_A,_R),(_A,_AB),(_A,_d),(_A,_S)))
if mibBuilder.loadTexts:portNotificationVarsGroup.setStatus(_B)
sFlowAgentGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,5))
sFlowAgentGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:sFlowAgentGroup.setStatus(_B)
portMirrorGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,6))
portMirrorGroup.setObjects(*((_A,_H),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AF)))
if mibBuilder.loadTexts:portMirrorGroup.setStatus(_B)
portSFlowCpGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,7))
portSFlowCpGroup.setObjects((_A,_AG))
if mibBuilder.loadTexts:portSFlowCpGroup.setStatus(_B)
portSFlowFsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,8))
portSFlowFsGroup.setObjects((_A,_AH))
if mibBuilder.loadTexts:portSFlowFsGroup.setStatus(_B)
mirrorConfigError=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,19,1,0,1))
mirrorConfigError.setObjects(*((_A,_K),(_A,_L),(_A,_Q),(_A,_R),(_A,_S),(_A,_d)))
if mibBuilder.loadTexts:mirrorConfigError.setStatus(_B)
monitorFileWritten=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,19,1,0,2))
monitorFileWritten.setObjects(*((_A,_K),(_A,_L),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:monitorFileWritten.setStatus(_B)
mirrorUnlikeNi=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,19,1,0,3))
mirrorUnlikeNi.setObjects(*((_A,_K),(_A,_L),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:mirrorUnlikeNi.setStatus(_B)
mirmonTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,1,4))
mirmonTrapsGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:mirmonTrapsGroup.setStatus(_B)
alcatelIND1PortMirMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,19,1,2,2,1))
alcatelIND1PortMirMonMIBCompliance.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:alcatelIND1PortMirMonMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MirMonErrorIds':MirMonErrorIds,'alcatelIND1PortMirrorMonitoringMIB':alcatelIND1PortMirrorMonitoringMIB,'alcatelIND1PortMirMonMIBNotifications':alcatelIND1PortMirMonMIBNotifications,_AI:mirrorConfigError,_AK:monitorFileWritten,_AJ:mirrorUnlikeNi,'alcatelIND1PortMirMonMIBObjects':alcatelIND1PortMirMonMIBObjects,'mirmonMirroring':mirmonMirroring,'mirrorTable':mirrorTable,'mirrorEntry':mirrorEntry,_H:mirrorSessionNumber,_U:mirrorMirroredIfindex,_V:mirrorMirroringIfindex,_W:mirrorStatus,_X:mirrorUnblockedVLAN,_Y:mirrorRowStatus,_Z:mirrorDirection,_a:mirrorSessOperStatus,_AF:mirrorTaggedVLAN,'mirrorSrcTable':mirrorSrcTable,'mirrorSrcEntry':mirrorSrcEntry,_T:mirrorSrcMirroredIf,_q:mirrorSrcStatus,_r:mirrorSrcDirection,_s:mirrorSrcRowStatus,_t:mirrorSrcOperStatus,'mirrorDstTable':mirrorDstTable,'mirrorDstEntry':mirrorDstEntry,_i:mirrorDstMirroringIf,_u:mirrorDstOperStatus,_v:mirrorDstAdminStatus,_w:mirrorDstRowStatus,'mirmonMonitoring':mirmonMonitoring,'monitorTable':monitorTable,'monitorEntry':monitorEntry,_P:monitorSessionNumber,_x:monitorIfindex,_y:monitorFileStatus,_b:monitorFileName,_c:monitorFileSize,_z:monitorScreenStatus,_A0:monitorScreenLine,_A1:monitorTrafficType,_A2:monitorStatus,_A3:monitorFileOverWrite,_A4:monitorDirection,_A5:monitorTimeout,_A6:monitorRowStatus,_A7:monitorCaptureType,'monitorSrcTable':monitorSrcTable,'monitorSrcEntry':monitorSrcEntry,_k:monitorSrcIfindex,_A8:monitorSrcStatus,_A9:monitorSrcDirection,_AA:monitorSrcRowStatus,'mirmonNotificationVars':mirmonNotificationVars,_K:mirmonPrimarySlot,_L:mirmonPrimaryPort,_Q:mirroringSlot,_R:mirroringPort,_AB:mirMonSession,_d:mirMonError,_S:mirMonErrorNi,'mirmonSFlowObjects':mirmonSFlowObjects,'alasFlowFsTable':alasFlowFsTable,_o:alasFlowFsEntry,_AH:alasFlowFsDeleteEntry,'alasFlowCpTable':alasFlowCpTable,_p:alasFlowCpEntry,_AG:alasFlowCpDeleteEntry,_AE:alasFlowAgentConfigType,_AD:alasFlowAgentAddressType,_AC:alasFlowAgentAddress,'alcatelIND1PortMirMonMIBConformance':alcatelIND1PortMirMonMIBConformance,'alcatelIND1PortMirMonMIBGroups':alcatelIND1PortMirMonMIBGroups,_AL:portMirroringGroup,_AM:portMonitoringGroup,_AN:portNotificationVarsGroup,'mirmonTrapsGroup':mirmonTrapsGroup,'sFlowAgentGroup':sFlowAgentGroup,'portMirrorGroup':portMirrorGroup,'portSFlowCpGroup':portSFlowCpGroup,'portSFlowFsGroup':portSFlowFsGroup,'alcatelIND1PortMirMonMIBCompliances':alcatelIND1PortMirMonMIBCompliances,'alcatelIND1PortMirMonMIBCompliance':alcatelIND1PortMirMonMIBCompliance})