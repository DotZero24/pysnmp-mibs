_P='lldpXdcbxFeatError'
_O='lldpXdcbxFeatAppProtoPriority'
_N='lldpXdcbxFeatPfcPriority'
_M='lldpXdcbxFeatPgBwAllocPgId'
_L='lldpXdcbxFeatPgPrioAllocPrioId'
_K='LldpXdcbxFeatureSubType'
_J='lldpXdcbxFeatSubType'
_I='lldpXdcbxFeatAppProtoIndex'
_H='percent'
_G='lldpXdcbxFeatType'
_F='TruthValue'
_E='lldpXdcbxPortNumber'
_D='read-write'
_C='read-only'
_B='LLDP-EXT-DCBX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LldpPortNumber,lldpExtensions=mibBuilder.importSymbols('LLDP-MIB','LldpPortNumber','lldpExtensions')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
lldpXdcbxMIB=ModuleIdentity((1,0,8802,1,1,2,1,5,6945))
class LldpXdcbxPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class LldpXdcbxPriorityGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('priorityGroupId0',0),('priorityGroupId1',1),('priorityGroupId2',2),('priorityGroupId3',3),('priorityGroupId4',4),('priorityGroupId5',5),('priorityGroupId6',6),('priorityGroupId7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('reserved14',14),('noBandwidthLimit',15)))
class LldpXdcbxFeatureType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('priorityGroup',2),('priorityFlowControl',3),('applicationProtocol',4)))
class LldpXdcbxFeatureSubType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class LldpXdcbxVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class LldpXdcbxTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class LldpXdcbxPgBw(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class LldpXdcbxTCPFC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
class LldpXdcbxAppProtos(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class LldpXdcbxSF(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('l2EtherType',0),('socketNumber',1),('reserved2',2),('reserved3',3)))
_LldpXdcbxNotifications_ObjectIdentity=ObjectIdentity
lldpXdcbxNotifications=_LldpXdcbxNotifications_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,0))
_LldpXdcbxObjects_ObjectIdentity=ObjectIdentity
lldpXdcbxObjects=_LldpXdcbxObjects_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,1))
_LldpXdcbxPortTable_Object=MibTable
lldpXdcbxPortTable=_LldpXdcbxPortTable_Object((1,0,8802,1,1,2,1,5,6945,1,1))
if mibBuilder.loadTexts:lldpXdcbxPortTable.setStatus(_A)
_LldpXdcbxPortEntry_Object=MibTableRow
lldpXdcbxPortEntry=_LldpXdcbxPortEntry_Object((1,0,8802,1,1,2,1,5,6945,1,1,1))
lldpXdcbxPortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:lldpXdcbxPortEntry.setStatus(_A)
_LldpXdcbxPortNumber_Type=LldpPortNumber
_LldpXdcbxPortNumber_Object=MibTableColumn
lldpXdcbxPortNumber=_LldpXdcbxPortNumber_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,1),_LldpXdcbxPortNumber_Type())
lldpXdcbxPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxPortNumber.setStatus(_A)
class _LldpXdcbxPortEnable_Type(TruthValue):defaultValue=1
_LldpXdcbxPortEnable_Type.__name__=_F
_LldpXdcbxPortEnable_Object=MibTableColumn
lldpXdcbxPortEnable=_LldpXdcbxPortEnable_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,2),_LldpXdcbxPortEnable_Type())
lldpXdcbxPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxPortEnable.setStatus(_A)
_LldpXdcbxPortVersionOper_Type=LldpXdcbxVersion
_LldpXdcbxPortVersionOper_Object=MibTableColumn
lldpXdcbxPortVersionOper=_LldpXdcbxPortVersionOper_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,3),_LldpXdcbxPortVersionOper_Type())
lldpXdcbxPortVersionOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxPortVersionOper.setStatus(_A)
_LldpXdcbxPortVersionMax_Type=LldpXdcbxVersion
_LldpXdcbxPortVersionMax_Object=MibTableColumn
lldpXdcbxPortVersionMax=_LldpXdcbxPortVersionMax_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,4),_LldpXdcbxPortVersionMax_Type())
lldpXdcbxPortVersionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxPortVersionMax.setStatus(_A)
_LldpXdcbxPortSeqNo_Type=Integer32
_LldpXdcbxPortSeqNo_Object=MibTableColumn
lldpXdcbxPortSeqNo=_LldpXdcbxPortSeqNo_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,5),_LldpXdcbxPortSeqNo_Type())
lldpXdcbxPortSeqNo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxPortSeqNo.setStatus(_A)
_LldpXdcbxPortAckNo_Type=Integer32
_LldpXdcbxPortAckNo_Object=MibTableColumn
lldpXdcbxPortAckNo=_LldpXdcbxPortAckNo_Object((1,0,8802,1,1,2,1,5,6945,1,1,1,6),_LldpXdcbxPortAckNo_Type())
lldpXdcbxPortAckNo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxPortAckNo.setStatus(_A)
_LldpXdcbxFeatures_ObjectIdentity=ObjectIdentity
lldpXdcbxFeatures=_LldpXdcbxFeatures_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,2))
_LldpXdcbxFeatTable_Object=MibTable
lldpXdcbxFeatTable=_LldpXdcbxFeatTable_Object((1,0,8802,1,1,2,1,5,6945,2,1))
if mibBuilder.loadTexts:lldpXdcbxFeatTable.setStatus(_A)
_LldpXdcbxFeatEntry_Object=MibTableRow
lldpXdcbxFeatEntry=_LldpXdcbxFeatEntry_Object((1,0,8802,1,1,2,1,5,6945,2,1,1))
lldpXdcbxFeatEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:lldpXdcbxFeatEntry.setStatus(_A)
_LldpXdcbxFeatType_Type=LldpXdcbxFeatureType
_LldpXdcbxFeatType_Object=MibTableColumn
lldpXdcbxFeatType=_LldpXdcbxFeatType_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,1),_LldpXdcbxFeatType_Type())
lldpXdcbxFeatType.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatType.setStatus(_A)
class _LldpXdcbxFeatSubType_Type(LldpXdcbxFeatureSubType):defaultValue=0
_LldpXdcbxFeatSubType_Type.__name__=_K
_LldpXdcbxFeatSubType_Object=MibTableColumn
lldpXdcbxFeatSubType=_LldpXdcbxFeatSubType_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,2),_LldpXdcbxFeatSubType_Type())
lldpXdcbxFeatSubType.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatSubType.setStatus(_A)
_LldpXdcbxFeatVersionOper_Type=LldpXdcbxVersion
_LldpXdcbxFeatVersionOper_Object=MibTableColumn
lldpXdcbxFeatVersionOper=_LldpXdcbxFeatVersionOper_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,3),_LldpXdcbxFeatVersionOper_Type())
lldpXdcbxFeatVersionOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatVersionOper.setStatus(_A)
_LldpXdcbxFeatVersionMax_Type=LldpXdcbxVersion
_LldpXdcbxFeatVersionMax_Object=MibTableColumn
lldpXdcbxFeatVersionMax=_LldpXdcbxFeatVersionMax_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,4),_LldpXdcbxFeatVersionMax_Type())
lldpXdcbxFeatVersionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatVersionMax.setStatus(_A)
class _LldpXdcbxFeatEnable_Type(TruthValue):defaultValue=1
_LldpXdcbxFeatEnable_Type.__name__=_F
_LldpXdcbxFeatEnable_Object=MibTableColumn
lldpXdcbxFeatEnable=_LldpXdcbxFeatEnable_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,5),_LldpXdcbxFeatEnable_Type())
lldpXdcbxFeatEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatEnable.setStatus(_A)
class _LldpXdcbxFeatWilling_Type(TruthValue):defaultValue=1
_LldpXdcbxFeatWilling_Type.__name__=_F
_LldpXdcbxFeatWilling_Object=MibTableColumn
lldpXdcbxFeatWilling=_LldpXdcbxFeatWilling_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,6),_LldpXdcbxFeatWilling_Type())
lldpXdcbxFeatWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatWilling.setStatus(_A)
class _LldpXdcbxFeatError_Type(TruthValue):defaultValue=2
_LldpXdcbxFeatError_Type.__name__=_F
_LldpXdcbxFeatError_Object=MibTableColumn
lldpXdcbxFeatError=_LldpXdcbxFeatError_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,7),_LldpXdcbxFeatError_Type())
lldpXdcbxFeatError.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatError.setStatus(_A)
_LldpXdcbxFeatAdvertise_Type=TruthValue
_LldpXdcbxFeatAdvertise_Object=MibTableColumn
lldpXdcbxFeatAdvertise=_LldpXdcbxFeatAdvertise_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,8),_LldpXdcbxFeatAdvertise_Type())
lldpXdcbxFeatAdvertise.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAdvertise.setStatus(_A)
_LldpXdcbxFeatOperMode_Type=TruthValue
_LldpXdcbxFeatOperMode_Object=MibTableColumn
lldpXdcbxFeatOperMode=_LldpXdcbxFeatOperMode_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,9),_LldpXdcbxFeatOperMode_Type())
lldpXdcbxFeatOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatOperMode.setStatus(_A)
_LldpXdcbxFeatSyncd_Type=TruthValue
_LldpXdcbxFeatSyncd_Object=MibTableColumn
lldpXdcbxFeatSyncd=_LldpXdcbxFeatSyncd_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,10),_LldpXdcbxFeatSyncd_Type())
lldpXdcbxFeatSyncd.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatSyncd.setStatus(_A)
_LldpXdcbxFeatSeqNo_Type=Integer32
_LldpXdcbxFeatSeqNo_Object=MibTableColumn
lldpXdcbxFeatSeqNo=_LldpXdcbxFeatSeqNo_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,11),_LldpXdcbxFeatSeqNo_Type())
lldpXdcbxFeatSeqNo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatSeqNo.setStatus(_A)
_LldpXdcbxFeatPeerWilling_Type=TruthValue
_LldpXdcbxFeatPeerWilling_Object=MibTableColumn
lldpXdcbxFeatPeerWilling=_LldpXdcbxFeatPeerWilling_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,12),_LldpXdcbxFeatPeerWilling_Type())
lldpXdcbxFeatPeerWilling.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPeerWilling.setStatus(_A)
_LldpXdcbxFeatLocalParameterChange_Type=TruthValue
_LldpXdcbxFeatLocalParameterChange_Object=MibTableColumn
lldpXdcbxFeatLocalParameterChange=_LldpXdcbxFeatLocalParameterChange_Object((1,0,8802,1,1,2,1,5,6945,2,1,1,13),_LldpXdcbxFeatLocalParameterChange_Type())
lldpXdcbxFeatLocalParameterChange.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatLocalParameterChange.setStatus(_A)
_LldpXdcbxFeatPg_ObjectIdentity=ObjectIdentity
lldpXdcbxFeatPg=_LldpXdcbxFeatPg_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,2,2))
_LldpXdcbxFeatPgNumTCsSupported_Type=LldpXdcbxTC
_LldpXdcbxFeatPgNumTCsSupported_Object=MibScalar
lldpXdcbxFeatPgNumTCsSupported=_LldpXdcbxFeatPgNumTCsSupported_Object((1,0,8802,1,1,2,1,5,6945,2,2,1),_LldpXdcbxFeatPgNumTCsSupported_Type())
lldpXdcbxFeatPgNumTCsSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPgNumTCsSupported.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocTable_Object=MibTable
lldpXdcbxFeatPgPrioAllocTable=_LldpXdcbxFeatPgPrioAllocTable_Object((1,0,8802,1,1,2,1,5,6945,2,2,2))
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocTable.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocEntry_Object=MibTableRow
lldpXdcbxFeatPgPrioAllocEntry=_LldpXdcbxFeatPgPrioAllocEntry_Object((1,0,8802,1,1,2,1,5,6945,2,2,2,1))
lldpXdcbxFeatPgPrioAllocEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocEntry.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocPrioId_Type=LldpXdcbxPriority
_LldpXdcbxFeatPgPrioAllocPrioId_Object=MibTableColumn
lldpXdcbxFeatPgPrioAllocPrioId=_LldpXdcbxFeatPgPrioAllocPrioId_Object((1,0,8802,1,1,2,1,5,6945,2,2,2,1,1),_LldpXdcbxFeatPgPrioAllocPrioId_Type())
lldpXdcbxFeatPgPrioAllocPrioId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocPrioId.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocPgIdDesired_Type=LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdDesired_Object=MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdDesired=_LldpXdcbxFeatPgPrioAllocPgIdDesired_Object((1,0,8802,1,1,2,1,5,6945,2,2,2,1,2),_LldpXdcbxFeatPgPrioAllocPgIdDesired_Type())
lldpXdcbxFeatPgPrioAllocPgIdDesired.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocPgIdDesired.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocPgIdOper_Type=LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdOper_Object=MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdOper=_LldpXdcbxFeatPgPrioAllocPgIdOper_Object((1,0,8802,1,1,2,1,5,6945,2,2,2,1,3),_LldpXdcbxFeatPgPrioAllocPgIdOper_Type())
lldpXdcbxFeatPgPrioAllocPgIdOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocPgIdOper.setStatus(_A)
_LldpXdcbxFeatPgPrioAllocPgIdPeer_Type=LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdPeer_Object=MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdPeer=_LldpXdcbxFeatPgPrioAllocPgIdPeer_Object((1,0,8802,1,1,2,1,5,6945,2,2,2,1,4),_LldpXdcbxFeatPgPrioAllocPgIdPeer_Type())
lldpXdcbxFeatPgPrioAllocPgIdPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPgPrioAllocPgIdPeer.setStatus(_A)
_LldpXdcbxFeatPgBwAllocTable_Object=MibTable
lldpXdcbxFeatPgBwAllocTable=_LldpXdcbxFeatPgBwAllocTable_Object((1,0,8802,1,1,2,1,5,6945,2,2,3))
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocTable.setStatus(_A)
_LldpXdcbxFeatPgBwAllocEntry_Object=MibTableRow
lldpXdcbxFeatPgBwAllocEntry=_LldpXdcbxFeatPgBwAllocEntry_Object((1,0,8802,1,1,2,1,5,6945,2,2,3,1))
lldpXdcbxFeatPgBwAllocEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocEntry.setStatus(_A)
_LldpXdcbxFeatPgBwAllocPgId_Type=LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgBwAllocPgId_Object=MibTableColumn
lldpXdcbxFeatPgBwAllocPgId=_LldpXdcbxFeatPgBwAllocPgId_Object((1,0,8802,1,1,2,1,5,6945,2,2,3,1,1),_LldpXdcbxFeatPgBwAllocPgId_Type())
lldpXdcbxFeatPgBwAllocPgId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocPgId.setStatus(_A)
_LldpXdcbxFeatPgBwAllocBwDesired_Type=LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwDesired_Object=MibTableColumn
lldpXdcbxFeatPgBwAllocBwDesired=_LldpXdcbxFeatPgBwAllocBwDesired_Object((1,0,8802,1,1,2,1,5,6945,2,2,3,1,2),_LldpXdcbxFeatPgBwAllocBwDesired_Type())
lldpXdcbxFeatPgBwAllocBwDesired.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwDesired.setStatus(_A)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwDesired.setUnits(_H)
_LldpXdcbxFeatPgBwAllocBwOper_Type=LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwOper_Object=MibTableColumn
lldpXdcbxFeatPgBwAllocBwOper=_LldpXdcbxFeatPgBwAllocBwOper_Object((1,0,8802,1,1,2,1,5,6945,2,2,3,1,3),_LldpXdcbxFeatPgBwAllocBwOper_Type())
lldpXdcbxFeatPgBwAllocBwOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwOper.setStatus(_A)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwOper.setUnits(_H)
_LldpXdcbxFeatPgBwAllocBwPeer_Type=LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwPeer_Object=MibTableColumn
lldpXdcbxFeatPgBwAllocBwPeer=_LldpXdcbxFeatPgBwAllocBwPeer_Object((1,0,8802,1,1,2,1,5,6945,2,2,3,1,4),_LldpXdcbxFeatPgBwAllocBwPeer_Type())
lldpXdcbxFeatPgBwAllocBwPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwPeer.setStatus(_A)
if mibBuilder.loadTexts:lldpXdcbxFeatPgBwAllocBwPeer.setUnits(_H)
_LldpXdcbxFeatPfc_ObjectIdentity=ObjectIdentity
lldpXdcbxFeatPfc=_LldpXdcbxFeatPfc_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,2,3))
_LldpXdcbxFeatPfcNumTCPFCSupported_Type=LldpXdcbxTCPFC
_LldpXdcbxFeatPfcNumTCPFCSupported_Object=MibScalar
lldpXdcbxFeatPfcNumTCPFCSupported=_LldpXdcbxFeatPfcNumTCPFCSupported_Object((1,0,8802,1,1,2,1,5,6945,2,3,1),_LldpXdcbxFeatPfcNumTCPFCSupported_Type())
lldpXdcbxFeatPfcNumTCPFCSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPfcNumTCPFCSupported.setStatus(_A)
_LldpXdcbxFeatPfcTable_Object=MibTable
lldpXdcbxFeatPfcTable=_LldpXdcbxFeatPfcTable_Object((1,0,8802,1,1,2,1,5,6945,2,3,2))
if mibBuilder.loadTexts:lldpXdcbxFeatPfcTable.setStatus(_A)
_LldpXdcbxFeatPfcEntry_Object=MibTableRow
lldpXdcbxFeatPfcEntry=_LldpXdcbxFeatPfcEntry_Object((1,0,8802,1,1,2,1,5,6945,2,3,2,1))
lldpXdcbxFeatPfcEntry.setIndexNames((0,_B,_E),(0,_B,_N))
if mibBuilder.loadTexts:lldpXdcbxFeatPfcEntry.setStatus(_A)
_LldpXdcbxFeatPfcPriority_Type=LldpXdcbxPriority
_LldpXdcbxFeatPfcPriority_Object=MibTableColumn
lldpXdcbxFeatPfcPriority=_LldpXdcbxFeatPfcPriority_Object((1,0,8802,1,1,2,1,5,6945,2,3,2,1,1),_LldpXdcbxFeatPfcPriority_Type())
lldpXdcbxFeatPfcPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPfcPriority.setStatus(_A)
_LldpXdcbxFeatPfcEnableDesired_Type=TruthValue
_LldpXdcbxFeatPfcEnableDesired_Object=MibTableColumn
lldpXdcbxFeatPfcEnableDesired=_LldpXdcbxFeatPfcEnableDesired_Object((1,0,8802,1,1,2,1,5,6945,2,3,2,1,2),_LldpXdcbxFeatPfcEnableDesired_Type())
lldpXdcbxFeatPfcEnableDesired.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatPfcEnableDesired.setStatus(_A)
_LldpXdcbxFeatPfcEnableOper_Type=TruthValue
_LldpXdcbxFeatPfcEnableOper_Object=MibTableColumn
lldpXdcbxFeatPfcEnableOper=_LldpXdcbxFeatPfcEnableOper_Object((1,0,8802,1,1,2,1,5,6945,2,3,2,1,3),_LldpXdcbxFeatPfcEnableOper_Type())
lldpXdcbxFeatPfcEnableOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPfcEnableOper.setStatus(_A)
_LldpXdcbxFeatPfcEnablePeer_Type=TruthValue
_LldpXdcbxFeatPfcEnablePeer_Object=MibTableColumn
lldpXdcbxFeatPfcEnablePeer=_LldpXdcbxFeatPfcEnablePeer_Object((1,0,8802,1,1,2,1,5,6945,2,3,2,1,4),_LldpXdcbxFeatPfcEnablePeer_Type())
lldpXdcbxFeatPfcEnablePeer.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatPfcEnablePeer.setStatus(_A)
_LldpXdcbxFeatAppProto_ObjectIdentity=ObjectIdentity
lldpXdcbxFeatAppProto=_LldpXdcbxFeatAppProto_ObjectIdentity((1,0,8802,1,1,2,1,5,6945,2,4))
_LldpXdcbxFeatAppProtoTable_Object=MibTable
lldpXdcbxFeatAppProtoTable=_LldpXdcbxFeatAppProtoTable_Object((1,0,8802,1,1,2,1,5,6945,2,4,1))
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoTable.setStatus(_A)
_LldpXdcbxFeatAppProtoEntry_Object=MibTableRow
lldpXdcbxFeatAppProtoEntry=_LldpXdcbxFeatAppProtoEntry_Object((1,0,8802,1,1,2,1,5,6945,2,4,1,1))
lldpXdcbxFeatAppProtoEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoEntry.setStatus(_A)
_LldpXdcbxFeatAppProtoIndex_Type=LldpXdcbxAppProtos
_LldpXdcbxFeatAppProtoIndex_Object=MibTableColumn
lldpXdcbxFeatAppProtoIndex=_LldpXdcbxFeatAppProtoIndex_Object((1,0,8802,1,1,2,1,5,6945,2,4,1,1,1),_LldpXdcbxFeatAppProtoIndex_Type())
lldpXdcbxFeatAppProtoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoIndex.setStatus(_A)
_LldpXdcbxFeatAppProtoSF_Type=LldpXdcbxSF
_LldpXdcbxFeatAppProtoSF_Object=MibTableColumn
lldpXdcbxFeatAppProtoSF=_LldpXdcbxFeatAppProtoSF_Object((1,0,8802,1,1,2,1,5,6945,2,4,1,1,2),_LldpXdcbxFeatAppProtoSF_Type())
lldpXdcbxFeatAppProtoSF.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoSF.setStatus(_A)
_LldpXdcbxFeatAppProtoOUI_Type=Integer32
_LldpXdcbxFeatAppProtoOUI_Object=MibTableColumn
lldpXdcbxFeatAppProtoOUI=_LldpXdcbxFeatAppProtoOUI_Object((1,0,8802,1,1,2,1,5,6945,2,4,1,1,3),_LldpXdcbxFeatAppProtoOUI_Type())
lldpXdcbxFeatAppProtoOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoOUI.setStatus(_A)
_LldpXdcbxFeatAppProtoId_Type=Integer32
_LldpXdcbxFeatAppProtoId_Object=MibTableColumn
lldpXdcbxFeatAppProtoId=_LldpXdcbxFeatAppProtoId_Object((1,0,8802,1,1,2,1,5,6945,2,4,1,1,4),_LldpXdcbxFeatAppProtoId_Type())
lldpXdcbxFeatAppProtoId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoId.setStatus(_A)
_LldpXdcbxFeatAppProtoPrioTable_Object=MibTable
lldpXdcbxFeatAppProtoPrioTable=_LldpXdcbxFeatAppProtoPrioTable_Object((1,0,8802,1,1,2,1,5,6945,2,4,2))
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoPrioTable.setStatus(_A)
_LldpXdcbxFeatAppProtoPrioEntry_Object=MibTableRow
lldpXdcbxFeatAppProtoPrioEntry=_LldpXdcbxFeatAppProtoPrioEntry_Object((1,0,8802,1,1,2,1,5,6945,2,4,2,1))
lldpXdcbxFeatAppProtoPrioEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_O))
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoPrioEntry.setStatus(_A)
_LldpXdcbxFeatAppProtoPriority_Type=LldpXdcbxPriority
_LldpXdcbxFeatAppProtoPriority_Object=MibTableColumn
lldpXdcbxFeatAppProtoPriority=_LldpXdcbxFeatAppProtoPriority_Object((1,0,8802,1,1,2,1,5,6945,2,4,2,1,1),_LldpXdcbxFeatAppProtoPriority_Type())
lldpXdcbxFeatAppProtoPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoPriority.setStatus(_A)
_LldpXdcbxFeatAppProtoEnableDesired_Type=TruthValue
_LldpXdcbxFeatAppProtoEnableDesired_Object=MibTableColumn
lldpXdcbxFeatAppProtoEnableDesired=_LldpXdcbxFeatAppProtoEnableDesired_Object((1,0,8802,1,1,2,1,5,6945,2,4,2,1,2),_LldpXdcbxFeatAppProtoEnableDesired_Type())
lldpXdcbxFeatAppProtoEnableDesired.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoEnableDesired.setStatus(_A)
_LldpXdcbxFeatAppProtoEnableOper_Type=TruthValue
_LldpXdcbxFeatAppProtoEnableOper_Object=MibTableColumn
lldpXdcbxFeatAppProtoEnableOper=_LldpXdcbxFeatAppProtoEnableOper_Object((1,0,8802,1,1,2,1,5,6945,2,4,2,1,3),_LldpXdcbxFeatAppProtoEnableOper_Type())
lldpXdcbxFeatAppProtoEnableOper.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoEnableOper.setStatus(_A)
_LldpXdcbxFeatAppProtoEnablePeer_Type=TruthValue
_LldpXdcbxFeatAppProtoEnablePeer_Object=MibTableColumn
lldpXdcbxFeatAppProtoEnablePeer=_LldpXdcbxFeatAppProtoEnablePeer_Object((1,0,8802,1,1,2,1,5,6945,2,4,2,1,4),_LldpXdcbxFeatAppProtoEnablePeer_Type())
lldpXdcbxFeatAppProtoEnablePeer.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdcbxFeatAppProtoEnablePeer.setStatus(_A)
lldpXdcbxMiscControlError=NotificationType((1,0,8802,1,1,2,1,5,6945,0,1))
lldpXdcbxMiscControlError.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxMiscControlError.setStatus(_A)
lldpXdcbxMiscFeatureError=NotificationType((1,0,8802,1,1,2,1,5,6945,0,2))
lldpXdcbxMiscFeatureError.setObjects((_B,_P))
if mibBuilder.loadTexts:lldpXdcbxMiscFeatureError.setStatus(_A)
lldpXdcbxMultiplePeers=NotificationType((1,0,8802,1,1,2,1,5,6945,0,3))
lldpXdcbxMultiplePeers.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxMultiplePeers.setStatus(_A)
lldpXdcbxLldpTxDisabled=NotificationType((1,0,8802,1,1,2,1,5,6945,0,4))
lldpXdcbxLldpTxDisabled.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxLldpTxDisabled.setStatus(_A)
lldpXdcbxLldpRxDisabled=NotificationType((1,0,8802,1,1,2,1,5,6945,0,5))
lldpXdcbxLldpRxDisabled.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxLldpRxDisabled.setStatus(_A)
lldpXdcbxDupControlTlv=NotificationType((1,0,8802,1,1,2,1,5,6945,0,6))
lldpXdcbxDupControlTlv.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxDupControlTlv.setStatus(_A)
lldpXdcbxDupFeatureTlv=NotificationType((1,0,8802,1,1,2,1,5,6945,0,7))
lldpXdcbxDupFeatureTlv.setObjects((_B,_G))
if mibBuilder.loadTexts:lldpXdcbxDupFeatureTlv.setStatus(_A)
lldpXdcbxPeerNoFeat=NotificationType((1,0,8802,1,1,2,1,5,6945,0,8))
lldpXdcbxPeerNoFeat.setObjects((_B,_G))
if mibBuilder.loadTexts:lldpXdcbxPeerNoFeat.setStatus(_A)
lldpXdcbxPeerNoResp=NotificationType((1,0,8802,1,1,2,1,5,6945,0,9))
lldpXdcbxPeerNoResp.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxPeerNoResp.setStatus(_A)
lldpXdcbxPeerConfigMismatch=NotificationType((1,0,8802,1,1,2,1,5,6945,0,10))
lldpXdcbxPeerConfigMismatch.setObjects((_B,_E))
if mibBuilder.loadTexts:lldpXdcbxPeerConfigMismatch.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LldpXdcbxPriority':LldpXdcbxPriority,'LldpXdcbxPriorityGroup':LldpXdcbxPriorityGroup,'LldpXdcbxFeatureType':LldpXdcbxFeatureType,_K:LldpXdcbxFeatureSubType,'LldpXdcbxVersion':LldpXdcbxVersion,'LldpXdcbxTC':LldpXdcbxTC,'LldpXdcbxPgBw':LldpXdcbxPgBw,'LldpXdcbxTCPFC':LldpXdcbxTCPFC,'LldpXdcbxAppProtos':LldpXdcbxAppProtos,'LldpXdcbxSF':LldpXdcbxSF,'lldpXdcbxMIB':lldpXdcbxMIB,'lldpXdcbxNotifications':lldpXdcbxNotifications,'lldpXdcbxMiscControlError':lldpXdcbxMiscControlError,'lldpXdcbxMiscFeatureError':lldpXdcbxMiscFeatureError,'lldpXdcbxMultiplePeers':lldpXdcbxMultiplePeers,'lldpXdcbxLldpTxDisabled':lldpXdcbxLldpTxDisabled,'lldpXdcbxLldpRxDisabled':lldpXdcbxLldpRxDisabled,'lldpXdcbxDupControlTlv':lldpXdcbxDupControlTlv,'lldpXdcbxDupFeatureTlv':lldpXdcbxDupFeatureTlv,'lldpXdcbxPeerNoFeat':lldpXdcbxPeerNoFeat,'lldpXdcbxPeerNoResp':lldpXdcbxPeerNoResp,'lldpXdcbxPeerConfigMismatch':lldpXdcbxPeerConfigMismatch,'lldpXdcbxObjects':lldpXdcbxObjects,'lldpXdcbxPortTable':lldpXdcbxPortTable,'lldpXdcbxPortEntry':lldpXdcbxPortEntry,_E:lldpXdcbxPortNumber,'lldpXdcbxPortEnable':lldpXdcbxPortEnable,'lldpXdcbxPortVersionOper':lldpXdcbxPortVersionOper,'lldpXdcbxPortVersionMax':lldpXdcbxPortVersionMax,'lldpXdcbxPortSeqNo':lldpXdcbxPortSeqNo,'lldpXdcbxPortAckNo':lldpXdcbxPortAckNo,'lldpXdcbxFeatures':lldpXdcbxFeatures,'lldpXdcbxFeatTable':lldpXdcbxFeatTable,'lldpXdcbxFeatEntry':lldpXdcbxFeatEntry,_G:lldpXdcbxFeatType,_J:lldpXdcbxFeatSubType,'lldpXdcbxFeatVersionOper':lldpXdcbxFeatVersionOper,'lldpXdcbxFeatVersionMax':lldpXdcbxFeatVersionMax,'lldpXdcbxFeatEnable':lldpXdcbxFeatEnable,'lldpXdcbxFeatWilling':lldpXdcbxFeatWilling,_P:lldpXdcbxFeatError,'lldpXdcbxFeatAdvertise':lldpXdcbxFeatAdvertise,'lldpXdcbxFeatOperMode':lldpXdcbxFeatOperMode,'lldpXdcbxFeatSyncd':lldpXdcbxFeatSyncd,'lldpXdcbxFeatSeqNo':lldpXdcbxFeatSeqNo,'lldpXdcbxFeatPeerWilling':lldpXdcbxFeatPeerWilling,'lldpXdcbxFeatLocalParameterChange':lldpXdcbxFeatLocalParameterChange,'lldpXdcbxFeatPg':lldpXdcbxFeatPg,'lldpXdcbxFeatPgNumTCsSupported':lldpXdcbxFeatPgNumTCsSupported,'lldpXdcbxFeatPgPrioAllocTable':lldpXdcbxFeatPgPrioAllocTable,'lldpXdcbxFeatPgPrioAllocEntry':lldpXdcbxFeatPgPrioAllocEntry,_L:lldpXdcbxFeatPgPrioAllocPrioId,'lldpXdcbxFeatPgPrioAllocPgIdDesired':lldpXdcbxFeatPgPrioAllocPgIdDesired,'lldpXdcbxFeatPgPrioAllocPgIdOper':lldpXdcbxFeatPgPrioAllocPgIdOper,'lldpXdcbxFeatPgPrioAllocPgIdPeer':lldpXdcbxFeatPgPrioAllocPgIdPeer,'lldpXdcbxFeatPgBwAllocTable':lldpXdcbxFeatPgBwAllocTable,'lldpXdcbxFeatPgBwAllocEntry':lldpXdcbxFeatPgBwAllocEntry,_M:lldpXdcbxFeatPgBwAllocPgId,'lldpXdcbxFeatPgBwAllocBwDesired':lldpXdcbxFeatPgBwAllocBwDesired,'lldpXdcbxFeatPgBwAllocBwOper':lldpXdcbxFeatPgBwAllocBwOper,'lldpXdcbxFeatPgBwAllocBwPeer':lldpXdcbxFeatPgBwAllocBwPeer,'lldpXdcbxFeatPfc':lldpXdcbxFeatPfc,'lldpXdcbxFeatPfcNumTCPFCSupported':lldpXdcbxFeatPfcNumTCPFCSupported,'lldpXdcbxFeatPfcTable':lldpXdcbxFeatPfcTable,'lldpXdcbxFeatPfcEntry':lldpXdcbxFeatPfcEntry,_N:lldpXdcbxFeatPfcPriority,'lldpXdcbxFeatPfcEnableDesired':lldpXdcbxFeatPfcEnableDesired,'lldpXdcbxFeatPfcEnableOper':lldpXdcbxFeatPfcEnableOper,'lldpXdcbxFeatPfcEnablePeer':lldpXdcbxFeatPfcEnablePeer,'lldpXdcbxFeatAppProto':lldpXdcbxFeatAppProto,'lldpXdcbxFeatAppProtoTable':lldpXdcbxFeatAppProtoTable,'lldpXdcbxFeatAppProtoEntry':lldpXdcbxFeatAppProtoEntry,_I:lldpXdcbxFeatAppProtoIndex,'lldpXdcbxFeatAppProtoSF':lldpXdcbxFeatAppProtoSF,'lldpXdcbxFeatAppProtoOUI':lldpXdcbxFeatAppProtoOUI,'lldpXdcbxFeatAppProtoId':lldpXdcbxFeatAppProtoId,'lldpXdcbxFeatAppProtoPrioTable':lldpXdcbxFeatAppProtoPrioTable,'lldpXdcbxFeatAppProtoPrioEntry':lldpXdcbxFeatAppProtoPrioEntry,_O:lldpXdcbxFeatAppProtoPriority,'lldpXdcbxFeatAppProtoEnableDesired':lldpXdcbxFeatAppProtoEnableDesired,'lldpXdcbxFeatAppProtoEnableOper':lldpXdcbxFeatAppProtoEnableOper,'lldpXdcbxFeatAppProtoEnablePeer':lldpXdcbxFeatAppProtoEnablePeer})