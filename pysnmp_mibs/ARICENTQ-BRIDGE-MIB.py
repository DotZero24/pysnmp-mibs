_o='fsDot1vProtocolPortGroupId'
_n='fsDot1vProtocolTemplateProtocolValue'
_m='fsDot1vProtocolTemplateFrameType'
_l='shared'
_k='independent'
_j='fsDot1qConstraintSet'
_i='fsDot1qConstraintVlan'
_h='VlanIndex'
_g='deleteOnTimeout'
_f='deleteOnReset'
_e='fsDot1qTpGroupAddress'
_d='fsDot1qTpFdbAddress'
_c='SnmpAdminString'
_b='EnabledStatus'
_a='OctetString'
_Z='fsDot1qVlanTimeMark'
_Y='fsDot1qStaticMulticastReceivePort'
_X='fsDot1qStaticMulticastAddress'
_W='permanent'
_V='fsDot1qStaticUnicastReceivePort'
_U='fsDot1qStaticUnicastAddress'
_T='delMember'
_S='addMember'
_R='invalid'
_Q='TruthValue'
_P='delForbidden'
_O='addForbidden'
_N='other'
_M='fsDot1qFdbId'
_L='fsDot1dBasePort'
_K='ARICENT-MIStdBRIDGE-MIB'
_J='fsDot1qTpPort'
_I='read-create'
_H='read-write'
_G='fsDot1qVlanIndex'
_F='not-accessible'
_E='fsDot1qVlanContextId'
_D='Integer32'
_C='read-only'
_B='ARICENTQ-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsDot1dBasePort,fsDot1dBridge=mibBuilder.importSymbols(_K,_L,'fsDot1dBridge')
EnabledStatus,=mibBuilder.importSymbols('ARICENTP-BRIDGE-MIB',_b)
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_c)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_Q)
fsQBridgeMIB=ModuleIdentity((1,3,6,1,4,1,2076,116,7))
if mibBuilder.loadTexts:fsQBridgeMIB.setRevisions(('2012-09-05 00:00',))
class VlanIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsQBridgeMIBObjects_ObjectIdentity=ObjectIdentity
fsQBridgeMIBObjects=_FsQBridgeMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1))
_FsDot1qBase_ObjectIdentity=ObjectIdentity
fsDot1qBase=_FsDot1qBase_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1,1))
_FsDot1qBaseTable_Object=MibTable
fsDot1qBaseTable=_FsDot1qBaseTable_Object((1,3,6,1,4,1,2076,116,7,1,1,1))
if mibBuilder.loadTexts:fsDot1qBaseTable.setStatus(_A)
_FsDot1qBaseEntry_Object=MibTableRow
fsDot1qBaseEntry=_FsDot1qBaseEntry_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1))
fsDot1qBaseEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsDot1qBaseEntry.setStatus(_A)
class _FsDot1qVlanContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qVlanContextId_Type.__name__=_D
_FsDot1qVlanContextId_Object=MibTableColumn
fsDot1qVlanContextId=_FsDot1qVlanContextId_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,1),_FsDot1qVlanContextId_Type())
fsDot1qVlanContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qVlanContextId.setStatus(_A)
class _FsDot1qVlanVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version1',1))
_FsDot1qVlanVersionNumber_Type.__name__=_D
_FsDot1qVlanVersionNumber_Object=MibTableColumn
fsDot1qVlanVersionNumber=_FsDot1qVlanVersionNumber_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,2),_FsDot1qVlanVersionNumber_Type())
fsDot1qVlanVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanVersionNumber.setStatus(_A)
_FsDot1qMaxVlanId_Type=VlanId
_FsDot1qMaxVlanId_Object=MibTableColumn
fsDot1qMaxVlanId=_FsDot1qMaxVlanId_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,3),_FsDot1qMaxVlanId_Type())
fsDot1qMaxVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qMaxVlanId.setStatus(_A)
_FsDot1qMaxSupportedVlans_Type=Unsigned32
_FsDot1qMaxSupportedVlans_Object=MibTableColumn
fsDot1qMaxSupportedVlans=_FsDot1qMaxSupportedVlans_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,4),_FsDot1qMaxSupportedVlans_Type())
fsDot1qMaxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qMaxSupportedVlans.setStatus(_A)
_FsDot1qNumVlans_Type=Unsigned32
_FsDot1qNumVlans_Object=MibTableColumn
fsDot1qNumVlans=_FsDot1qNumVlans_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,5),_FsDot1qNumVlans_Type())
fsDot1qNumVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qNumVlans.setStatus(_A)
_FsDot1qGvrpStatus_Type=EnabledStatus
_FsDot1qGvrpStatus_Object=MibTableColumn
fsDot1qGvrpStatus=_FsDot1qGvrpStatus_Object((1,3,6,1,4,1,2076,116,7,1,1,1,1,6),_FsDot1qGvrpStatus_Type())
fsDot1qGvrpStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qGvrpStatus.setStatus(_A)
_FsDot1qTp_ObjectIdentity=ObjectIdentity
fsDot1qTp=_FsDot1qTp_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1,2))
_FsDot1qFdbTable_Object=MibTable
fsDot1qFdbTable=_FsDot1qFdbTable_Object((1,3,6,1,4,1,2076,116,7,1,2,1))
if mibBuilder.loadTexts:fsDot1qFdbTable.setStatus(_A)
_FsDot1qFdbEntry_Object=MibTableRow
fsDot1qFdbEntry=_FsDot1qFdbEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,1,1))
fsDot1qFdbEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:fsDot1qFdbEntry.setStatus(_A)
_FsDot1qFdbId_Type=Unsigned32
_FsDot1qFdbId_Object=MibTableColumn
fsDot1qFdbId=_FsDot1qFdbId_Object((1,3,6,1,4,1,2076,116,7,1,2,1,1,1),_FsDot1qFdbId_Type())
fsDot1qFdbId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qFdbId.setStatus(_A)
_FsDot1qFdbDynamicCount_Type=Counter32
_FsDot1qFdbDynamicCount_Object=MibTableColumn
fsDot1qFdbDynamicCount=_FsDot1qFdbDynamicCount_Object((1,3,6,1,4,1,2076,116,7,1,2,1,1,2),_FsDot1qFdbDynamicCount_Type())
fsDot1qFdbDynamicCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qFdbDynamicCount.setStatus(_A)
_FsDot1qTpFdbTable_Object=MibTable
fsDot1qTpFdbTable=_FsDot1qTpFdbTable_Object((1,3,6,1,4,1,2076,116,7,1,2,2))
if mibBuilder.loadTexts:fsDot1qTpFdbTable.setStatus(_A)
_FsDot1qTpFdbEntry_Object=MibTableRow
fsDot1qTpFdbEntry=_FsDot1qTpFdbEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,2,1))
fsDot1qTpFdbEntry.setIndexNames((0,_B,_E),(0,_B,_M),(0,_B,_d))
if mibBuilder.loadTexts:fsDot1qTpFdbEntry.setStatus(_A)
_FsDot1qTpFdbAddress_Type=MacAddress
_FsDot1qTpFdbAddress_Object=MibTableColumn
fsDot1qTpFdbAddress=_FsDot1qTpFdbAddress_Object((1,3,6,1,4,1,2076,116,7,1,2,2,1,1),_FsDot1qTpFdbAddress_Type())
fsDot1qTpFdbAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qTpFdbAddress.setStatus(_A)
class _FsDot1qTpFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qTpFdbPort_Type.__name__=_D
_FsDot1qTpFdbPort_Object=MibTableColumn
fsDot1qTpFdbPort=_FsDot1qTpFdbPort_Object((1,3,6,1,4,1,2076,116,7,1,2,2,1,2),_FsDot1qTpFdbPort_Type())
fsDot1qTpFdbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpFdbPort.setStatus(_A)
class _FsDot1qTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_R,2),('learned',3),('self',4),('mgmt',5)))
_FsDot1qTpFdbStatus_Type.__name__=_D
_FsDot1qTpFdbStatus_Object=MibTableColumn
fsDot1qTpFdbStatus=_FsDot1qTpFdbStatus_Object((1,3,6,1,4,1,2076,116,7,1,2,2,1,3),_FsDot1qTpFdbStatus_Type())
fsDot1qTpFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpFdbStatus.setStatus(_A)
_FsDot1qTpFdbPw_Type=Unsigned32
_FsDot1qTpFdbPw_Object=MibTableColumn
fsDot1qTpFdbPw=_FsDot1qTpFdbPw_Object((1,3,6,1,4,1,2076,116,7,1,2,2,1,4),_FsDot1qTpFdbPw_Type())
fsDot1qTpFdbPw.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpFdbPw.setStatus(_A)
_FsDot1qTpGroupTable_Object=MibTable
fsDot1qTpGroupTable=_FsDot1qTpGroupTable_Object((1,3,6,1,4,1,2076,116,7,1,2,3))
if mibBuilder.loadTexts:fsDot1qTpGroupTable.setStatus(_A)
_FsDot1qTpGroupEntry_Object=MibTableRow
fsDot1qTpGroupEntry=_FsDot1qTpGroupEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,3,1))
fsDot1qTpGroupEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_e),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qTpGroupEntry.setStatus(_A)
_FsDot1qVlanIndex_Type=VlanIndex
_FsDot1qVlanIndex_Object=MibTableColumn
fsDot1qVlanIndex=_FsDot1qVlanIndex_Object((1,3,6,1,4,1,2076,116,7,1,2,3,1,1),_FsDot1qVlanIndex_Type())
fsDot1qVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qVlanIndex.setStatus(_A)
_FsDot1qTpGroupAddress_Type=MacAddress
_FsDot1qTpGroupAddress_Object=MibTableColumn
fsDot1qTpGroupAddress=_FsDot1qTpGroupAddress_Object((1,3,6,1,4,1,2076,116,7,1,2,3,1,2),_FsDot1qTpGroupAddress_Type())
fsDot1qTpGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qTpGroupAddress.setStatus(_A)
class _FsDot1qTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDot1qTpPort_Type.__name__=_D
_FsDot1qTpPort_Object=MibTableColumn
fsDot1qTpPort=_FsDot1qTpPort_Object((1,3,6,1,4,1,2076,116,7,1,2,3,1,3),_FsDot1qTpPort_Type())
fsDot1qTpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qTpPort.setStatus(_A)
_FsDot1qTpGroupIsLearnt_Type=TruthValue
_FsDot1qTpGroupIsLearnt_Object=MibTableColumn
fsDot1qTpGroupIsLearnt=_FsDot1qTpGroupIsLearnt_Object((1,3,6,1,4,1,2076,116,7,1,2,3,1,4),_FsDot1qTpGroupIsLearnt_Type())
fsDot1qTpGroupIsLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpGroupIsLearnt.setStatus(_A)
_FsDot1qForwardAllLearntPortTable_Object=MibTable
fsDot1qForwardAllLearntPortTable=_FsDot1qForwardAllLearntPortTable_Object((1,3,6,1,4,1,2076,116,7,1,2,4))
if mibBuilder.loadTexts:fsDot1qForwardAllLearntPortTable.setStatus(_A)
_FsDot1qForwardAllLearntPortEntry_Object=MibTableRow
fsDot1qForwardAllLearntPortEntry=_FsDot1qForwardAllLearntPortEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,4,1))
fsDot1qForwardAllLearntPortEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qForwardAllLearntPortEntry.setStatus(_A)
_FsDot1qForwardAllIsLearnt_Type=TruthValue
_FsDot1qForwardAllIsLearnt_Object=MibTableColumn
fsDot1qForwardAllIsLearnt=_FsDot1qForwardAllIsLearnt_Object((1,3,6,1,4,1,2076,116,7,1,2,4,1,1),_FsDot1qForwardAllIsLearnt_Type())
fsDot1qForwardAllIsLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qForwardAllIsLearnt.setStatus(_A)
_FsDot1qForwardAllStatusTable_Object=MibTable
fsDot1qForwardAllStatusTable=_FsDot1qForwardAllStatusTable_Object((1,3,6,1,4,1,2076,116,7,1,2,5))
if mibBuilder.loadTexts:fsDot1qForwardAllStatusTable.setStatus(_A)
_FsDot1qForwardAllStatusEntry_Object=MibTableRow
fsDot1qForwardAllStatusEntry=_FsDot1qForwardAllStatusEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,5,1))
fsDot1qForwardAllStatusEntry.setIndexNames((0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qForwardAllStatusEntry.setStatus(_A)
_FsDot1qForwardAllRowStatus_Type=RowStatus
_FsDot1qForwardAllRowStatus_Object=MibTableColumn
fsDot1qForwardAllRowStatus=_FsDot1qForwardAllRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,2,5,1,1),_FsDot1qForwardAllRowStatus_Type())
fsDot1qForwardAllRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qForwardAllRowStatus.setStatus(_A)
_FsDot1qForwardAllPortConfigTable_Object=MibTable
fsDot1qForwardAllPortConfigTable=_FsDot1qForwardAllPortConfigTable_Object((1,3,6,1,4,1,2076,116,7,1,2,6))
if mibBuilder.loadTexts:fsDot1qForwardAllPortConfigTable.setStatus(_A)
_FsDot1qForwardAllPortConfigEntry_Object=MibTableRow
fsDot1qForwardAllPortConfigEntry=_FsDot1qForwardAllPortConfigEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,6,1))
fsDot1qForwardAllPortConfigEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qForwardAllPortConfigEntry.setStatus(_A)
class _FsDot1qForwardAllPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_O,2),(_T,3),(_P,4)))
_FsDot1qForwardAllPort_Type.__name__=_D
_FsDot1qForwardAllPort_Object=MibTableColumn
fsDot1qForwardAllPort=_FsDot1qForwardAllPort_Object((1,3,6,1,4,1,2076,116,7,1,2,6,1,1),_FsDot1qForwardAllPort_Type())
fsDot1qForwardAllPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qForwardAllPort.setStatus(_A)
_FsDot1qForwardUnregLearntPortTable_Object=MibTable
fsDot1qForwardUnregLearntPortTable=_FsDot1qForwardUnregLearntPortTable_Object((1,3,6,1,4,1,2076,116,7,1,2,7))
if mibBuilder.loadTexts:fsDot1qForwardUnregLearntPortTable.setStatus(_A)
_FsDot1qForwardUnregLearntPortEntry_Object=MibTableRow
fsDot1qForwardUnregLearntPortEntry=_FsDot1qForwardUnregLearntPortEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,7,1))
fsDot1qForwardUnregLearntPortEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qForwardUnregLearntPortEntry.setStatus(_A)
_FsDot1qForwardUnregIsLearnt_Type=TruthValue
_FsDot1qForwardUnregIsLearnt_Object=MibTableColumn
fsDot1qForwardUnregIsLearnt=_FsDot1qForwardUnregIsLearnt_Object((1,3,6,1,4,1,2076,116,7,1,2,7,1,1),_FsDot1qForwardUnregIsLearnt_Type())
fsDot1qForwardUnregIsLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qForwardUnregIsLearnt.setStatus(_A)
_FsDot1qForwardUnregStatusTable_Object=MibTable
fsDot1qForwardUnregStatusTable=_FsDot1qForwardUnregStatusTable_Object((1,3,6,1,4,1,2076,116,7,1,2,8))
if mibBuilder.loadTexts:fsDot1qForwardUnregStatusTable.setStatus(_A)
_FsDot1qForwardUnregStatusEntry_Object=MibTableRow
fsDot1qForwardUnregStatusEntry=_FsDot1qForwardUnregStatusEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,8,1))
fsDot1qForwardUnregStatusEntry.setIndexNames((0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qForwardUnregStatusEntry.setStatus(_A)
_FsDot1qForwardUnregRowStatus_Type=RowStatus
_FsDot1qForwardUnregRowStatus_Object=MibTableColumn
fsDot1qForwardUnregRowStatus=_FsDot1qForwardUnregRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,2,8,1,1),_FsDot1qForwardUnregRowStatus_Type())
fsDot1qForwardUnregRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qForwardUnregRowStatus.setStatus(_A)
_FsDot1qForwardUnregPortConfigTable_Object=MibTable
fsDot1qForwardUnregPortConfigTable=_FsDot1qForwardUnregPortConfigTable_Object((1,3,6,1,4,1,2076,116,7,1,2,9))
if mibBuilder.loadTexts:fsDot1qForwardUnregPortConfigTable.setStatus(_A)
_FsDot1qForwardUnregPortConfigEntry_Object=MibTableRow
fsDot1qForwardUnregPortConfigEntry=_FsDot1qForwardUnregPortConfigEntry_Object((1,3,6,1,4,1,2076,116,7,1,2,9,1))
fsDot1qForwardUnregPortConfigEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qForwardUnregPortConfigEntry.setStatus(_A)
class _FsDot1qForwardUnregPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_O,2),(_T,3),(_P,4)))
_FsDot1qForwardUnregPort_Type.__name__=_D
_FsDot1qForwardUnregPort_Object=MibTableColumn
fsDot1qForwardUnregPort=_FsDot1qForwardUnregPort_Object((1,3,6,1,4,1,2076,116,7,1,2,9,1,1),_FsDot1qForwardUnregPort_Type())
fsDot1qForwardUnregPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qForwardUnregPort.setStatus(_A)
_FsDot1qStatic_ObjectIdentity=ObjectIdentity
fsDot1qStatic=_FsDot1qStatic_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1,3))
_FsDot1qStaticUnicastTable_Object=MibTable
fsDot1qStaticUnicastTable=_FsDot1qStaticUnicastTable_Object((1,3,6,1,4,1,2076,116,7,1,3,1))
if mibBuilder.loadTexts:fsDot1qStaticUnicastTable.setStatus(_A)
_FsDot1qStaticUnicastEntry_Object=MibTableRow
fsDot1qStaticUnicastEntry=_FsDot1qStaticUnicastEntry_Object((1,3,6,1,4,1,2076,116,7,1,3,1,1))
fsDot1qStaticUnicastEntry.setIndexNames((0,_B,_E),(0,_B,_M),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:fsDot1qStaticUnicastEntry.setStatus(_A)
_FsDot1qStaticUnicastAddress_Type=MacAddress
_FsDot1qStaticUnicastAddress_Object=MibTableColumn
fsDot1qStaticUnicastAddress=_FsDot1qStaticUnicastAddress_Object((1,3,6,1,4,1,2076,116,7,1,3,1,1,1),_FsDot1qStaticUnicastAddress_Type())
fsDot1qStaticUnicastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qStaticUnicastAddress.setStatus(_A)
class _FsDot1qStaticUnicastReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qStaticUnicastReceivePort_Type.__name__=_D
_FsDot1qStaticUnicastReceivePort_Object=MibTableColumn
fsDot1qStaticUnicastReceivePort=_FsDot1qStaticUnicastReceivePort_Object((1,3,6,1,4,1,2076,116,7,1,3,1,1,2),_FsDot1qStaticUnicastReceivePort_Type())
fsDot1qStaticUnicastReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qStaticUnicastReceivePort.setStatus(_A)
_FsDot1qStaticUnicastRowStatus_Type=RowStatus
_FsDot1qStaticUnicastRowStatus_Object=MibTableColumn
fsDot1qStaticUnicastRowStatus=_FsDot1qStaticUnicastRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,3,1,1,3),_FsDot1qStaticUnicastRowStatus_Type())
fsDot1qStaticUnicastRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qStaticUnicastRowStatus.setStatus(_A)
class _FsDot1qStaticUnicastStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_R,2),(_W,3),(_f,4),(_g,5)))
_FsDot1qStaticUnicastStatus_Type.__name__=_D
_FsDot1qStaticUnicastStatus_Object=MibTableColumn
fsDot1qStaticUnicastStatus=_FsDot1qStaticUnicastStatus_Object((1,3,6,1,4,1,2076,116,7,1,3,1,1,4),_FsDot1qStaticUnicastStatus_Type())
fsDot1qStaticUnicastStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qStaticUnicastStatus.setStatus(_A)
_FsDot1qStaticAllowedToGoTable_Object=MibTable
fsDot1qStaticAllowedToGoTable=_FsDot1qStaticAllowedToGoTable_Object((1,3,6,1,4,1,2076,116,7,1,3,2))
if mibBuilder.loadTexts:fsDot1qStaticAllowedToGoTable.setStatus(_A)
_FsDot1qStaticAllowedToGoEntry_Object=MibTableRow
fsDot1qStaticAllowedToGoEntry=_FsDot1qStaticAllowedToGoEntry_Object((1,3,6,1,4,1,2076,116,7,1,3,2,1))
fsDot1qStaticAllowedToGoEntry.setIndexNames((0,_B,_E),(0,_B,_M),(0,_B,_U),(0,_B,_V),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qStaticAllowedToGoEntry.setStatus(_A)
_FsDot1qStaticAllowedIsMember_Type=TruthValue
_FsDot1qStaticAllowedIsMember_Object=MibTableColumn
fsDot1qStaticAllowedIsMember=_FsDot1qStaticAllowedIsMember_Object((1,3,6,1,4,1,2076,116,7,1,3,2,1,1),_FsDot1qStaticAllowedIsMember_Type())
fsDot1qStaticAllowedIsMember.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qStaticAllowedIsMember.setStatus(_A)
_FsDot1qStaticMulticastTable_Object=MibTable
fsDot1qStaticMulticastTable=_FsDot1qStaticMulticastTable_Object((1,3,6,1,4,1,2076,116,7,1,3,3))
if mibBuilder.loadTexts:fsDot1qStaticMulticastTable.setStatus(_A)
_FsDot1qStaticMulticastEntry_Object=MibTableRow
fsDot1qStaticMulticastEntry=_FsDot1qStaticMulticastEntry_Object((1,3,6,1,4,1,2076,116,7,1,3,3,1))
fsDot1qStaticMulticastEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:fsDot1qStaticMulticastEntry.setStatus(_A)
_FsDot1qStaticMulticastAddress_Type=MacAddress
_FsDot1qStaticMulticastAddress_Object=MibTableColumn
fsDot1qStaticMulticastAddress=_FsDot1qStaticMulticastAddress_Object((1,3,6,1,4,1,2076,116,7,1,3,3,1,1),_FsDot1qStaticMulticastAddress_Type())
fsDot1qStaticMulticastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qStaticMulticastAddress.setStatus(_A)
class _FsDot1qStaticMulticastReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qStaticMulticastReceivePort_Type.__name__=_D
_FsDot1qStaticMulticastReceivePort_Object=MibTableColumn
fsDot1qStaticMulticastReceivePort=_FsDot1qStaticMulticastReceivePort_Object((1,3,6,1,4,1,2076,116,7,1,3,3,1,2),_FsDot1qStaticMulticastReceivePort_Type())
fsDot1qStaticMulticastReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qStaticMulticastReceivePort.setStatus(_A)
_FsDot1qStaticMulticastRowStatus_Type=RowStatus
_FsDot1qStaticMulticastRowStatus_Object=MibTableColumn
fsDot1qStaticMulticastRowStatus=_FsDot1qStaticMulticastRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,3,3,1,3),_FsDot1qStaticMulticastRowStatus_Type())
fsDot1qStaticMulticastRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qStaticMulticastRowStatus.setStatus(_A)
class _FsDot1qStaticMulticastStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_R,2),(_W,3),(_f,4),(_g,5)))
_FsDot1qStaticMulticastStatus_Type.__name__=_D
_FsDot1qStaticMulticastStatus_Object=MibTableColumn
fsDot1qStaticMulticastStatus=_FsDot1qStaticMulticastStatus_Object((1,3,6,1,4,1,2076,116,7,1,3,3,1,4),_FsDot1qStaticMulticastStatus_Type())
fsDot1qStaticMulticastStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qStaticMulticastStatus.setStatus(_A)
_FsDot1qStaticMcastPortTable_Object=MibTable
fsDot1qStaticMcastPortTable=_FsDot1qStaticMcastPortTable_Object((1,3,6,1,4,1,2076,116,7,1,3,4))
if mibBuilder.loadTexts:fsDot1qStaticMcastPortTable.setStatus(_A)
_FsDot1qStaticMcastPortEntry_Object=MibTableRow
fsDot1qStaticMcastPortEntry=_FsDot1qStaticMcastPortEntry_Object((1,3,6,1,4,1,2076,116,7,1,3,4,1))
fsDot1qStaticMcastPortEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_X),(0,_B,_Y),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qStaticMcastPortEntry.setStatus(_A)
class _FsDot1qStaticMcastPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_O,2),(_T,3),(_P,4)))
_FsDot1qStaticMcastPort_Type.__name__=_D
_FsDot1qStaticMcastPort_Object=MibTableColumn
fsDot1qStaticMcastPort=_FsDot1qStaticMcastPort_Object((1,3,6,1,4,1,2076,116,7,1,3,4,1,1),_FsDot1qStaticMcastPort_Type())
fsDot1qStaticMcastPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qStaticMcastPort.setStatus(_A)
_FsDot1qVlan_ObjectIdentity=ObjectIdentity
fsDot1qVlan=_FsDot1qVlan_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1,4))
_FsDot1qVlanNumDeletesTable_Object=MibTable
fsDot1qVlanNumDeletesTable=_FsDot1qVlanNumDeletesTable_Object((1,3,6,1,4,1,2076,116,7,1,4,1))
if mibBuilder.loadTexts:fsDot1qVlanNumDeletesTable.setStatus(_A)
_FsDot1qVlanNumDeletesEntry_Object=MibTableRow
fsDot1qVlanNumDeletesEntry=_FsDot1qVlanNumDeletesEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,1,1))
fsDot1qVlanNumDeletesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsDot1qVlanNumDeletesEntry.setStatus(_A)
_FsDot1qVlanNumDeletes_Type=Counter32
_FsDot1qVlanNumDeletes_Object=MibTableColumn
fsDot1qVlanNumDeletes=_FsDot1qVlanNumDeletes_Object((1,3,6,1,4,1,2076,116,7,1,4,1,1,1),_FsDot1qVlanNumDeletes_Type())
fsDot1qVlanNumDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanNumDeletes.setStatus(_A)
_FsDot1qVlanCurrentTable_Object=MibTable
fsDot1qVlanCurrentTable=_FsDot1qVlanCurrentTable_Object((1,3,6,1,4,1,2076,116,7,1,4,2))
if mibBuilder.loadTexts:fsDot1qVlanCurrentTable.setStatus(_A)
_FsDot1qVlanCurrentEntry_Object=MibTableRow
fsDot1qVlanCurrentEntry=_FsDot1qVlanCurrentEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,2,1))
fsDot1qVlanCurrentEntry.setIndexNames((0,_B,_E),(0,_B,_Z),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qVlanCurrentEntry.setStatus(_A)
_FsDot1qVlanTimeMark_Type=TimeFilter
_FsDot1qVlanTimeMark_Object=MibTableColumn
fsDot1qVlanTimeMark=_FsDot1qVlanTimeMark_Object((1,3,6,1,4,1,2076,116,7,1,4,2,1,1),_FsDot1qVlanTimeMark_Type())
fsDot1qVlanTimeMark.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qVlanTimeMark.setStatus(_A)
_FsDot1qVlanFdbId_Type=Unsigned32
_FsDot1qVlanFdbId_Object=MibTableColumn
fsDot1qVlanFdbId=_FsDot1qVlanFdbId_Object((1,3,6,1,4,1,2076,116,7,1,4,2,1,2),_FsDot1qVlanFdbId_Type())
fsDot1qVlanFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanFdbId.setStatus(_A)
class _FsDot1qVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_W,2),('dynamicGvrp',3)))
_FsDot1qVlanStatus_Type.__name__=_D
_FsDot1qVlanStatus_Object=MibTableColumn
fsDot1qVlanStatus=_FsDot1qVlanStatus_Object((1,3,6,1,4,1,2076,116,7,1,4,2,1,3),_FsDot1qVlanStatus_Type())
fsDot1qVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanStatus.setStatus(_A)
_FsDot1qVlanCreationTime_Type=TimeTicks
_FsDot1qVlanCreationTime_Object=MibTableColumn
fsDot1qVlanCreationTime=_FsDot1qVlanCreationTime_Object((1,3,6,1,4,1,2076,116,7,1,4,2,1,4),_FsDot1qVlanCreationTime_Type())
fsDot1qVlanCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanCreationTime.setStatus(_A)
_FsDot1qVlanEgressPortTable_Object=MibTable
fsDot1qVlanEgressPortTable=_FsDot1qVlanEgressPortTable_Object((1,3,6,1,4,1,2076,116,7,1,4,3))
if mibBuilder.loadTexts:fsDot1qVlanEgressPortTable.setStatus(_A)
_FsDot1qVlanEgressPortEntry_Object=MibTableRow
fsDot1qVlanEgressPortEntry=_FsDot1qVlanEgressPortEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,3,1))
fsDot1qVlanEgressPortEntry.setIndexNames((0,_B,_E),(0,_B,_Z),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qVlanEgressPortEntry.setStatus(_A)
class _FsDot1qVlanCurrentEgressPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tagged',1),('untagged',2)))
_FsDot1qVlanCurrentEgressPort_Type.__name__=_D
_FsDot1qVlanCurrentEgressPort_Object=MibTableColumn
fsDot1qVlanCurrentEgressPort=_FsDot1qVlanCurrentEgressPort_Object((1,3,6,1,4,1,2076,116,7,1,4,3,1,1),_FsDot1qVlanCurrentEgressPort_Type())
fsDot1qVlanCurrentEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qVlanCurrentEgressPort.setStatus(_A)
_FsDot1qVlanStaticTable_Object=MibTable
fsDot1qVlanStaticTable=_FsDot1qVlanStaticTable_Object((1,3,6,1,4,1,2076,116,7,1,4,4))
if mibBuilder.loadTexts:fsDot1qVlanStaticTable.setStatus(_A)
_FsDot1qVlanStaticEntry_Object=MibTableRow
fsDot1qVlanStaticEntry=_FsDot1qVlanStaticEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,4,1))
fsDot1qVlanStaticEntry.setIndexNames((0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qVlanStaticEntry.setStatus(_A)
class _FsDot1qVlanStaticName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDot1qVlanStaticName_Type.__name__=_c
_FsDot1qVlanStaticName_Object=MibTableColumn
fsDot1qVlanStaticName=_FsDot1qVlanStaticName_Object((1,3,6,1,4,1,2076,116,7,1,4,4,1,1),_FsDot1qVlanStaticName_Type())
fsDot1qVlanStaticName.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qVlanStaticName.setStatus(_A)
_FsDot1qVlanStaticRowStatus_Type=RowStatus
_FsDot1qVlanStaticRowStatus_Object=MibTableColumn
fsDot1qVlanStaticRowStatus=_FsDot1qVlanStaticRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,4,4,1,2),_FsDot1qVlanStaticRowStatus_Type())
fsDot1qVlanStaticRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qVlanStaticRowStatus.setStatus(_A)
_FsDot1qVlanStaticPortConfigTable_Object=MibTable
fsDot1qVlanStaticPortConfigTable=_FsDot1qVlanStaticPortConfigTable_Object((1,3,6,1,4,1,2076,116,7,1,4,5))
if mibBuilder.loadTexts:fsDot1qVlanStaticPortConfigTable.setStatus(_A)
_FsDot1qVlanStaticPortConfigEntry_Object=MibTableRow
fsDot1qVlanStaticPortConfigEntry=_FsDot1qVlanStaticPortConfigEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,5,1))
fsDot1qVlanStaticPortConfigEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:fsDot1qVlanStaticPortConfigEntry.setStatus(_A)
class _FsDot1qVlanStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('addTagged',1),('addUntagged',2),(_O,3),('delTagged',4),('delUntagged',5),(_P,6)))
_FsDot1qVlanStaticPort_Type.__name__=_D
_FsDot1qVlanStaticPort_Object=MibTableColumn
fsDot1qVlanStaticPort=_FsDot1qVlanStaticPort_Object((1,3,6,1,4,1,2076,116,7,1,4,5,1,1),_FsDot1qVlanStaticPort_Type())
fsDot1qVlanStaticPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qVlanStaticPort.setStatus(_A)
_FsDot1qNextFreeLocalVlanIndexTable_Object=MibTable
fsDot1qNextFreeLocalVlanIndexTable=_FsDot1qNextFreeLocalVlanIndexTable_Object((1,3,6,1,4,1,2076,116,7,1,4,6))
if mibBuilder.loadTexts:fsDot1qNextFreeLocalVlanIndexTable.setStatus(_A)
_FsDot1qNextFreeLocalVlanIndexEntry_Object=MibTableRow
fsDot1qNextFreeLocalVlanIndexEntry=_FsDot1qNextFreeLocalVlanIndexEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,6,1))
fsDot1qNextFreeLocalVlanIndexEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsDot1qNextFreeLocalVlanIndexEntry.setStatus(_A)
class _FsDot1qNextFreeLocalVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4096,2147483647))
_FsDot1qNextFreeLocalVlanIndex_Type.__name__=_D
_FsDot1qNextFreeLocalVlanIndex_Object=MibTableColumn
fsDot1qNextFreeLocalVlanIndex=_FsDot1qNextFreeLocalVlanIndex_Object((1,3,6,1,4,1,2076,116,7,1,4,6,1,1),_FsDot1qNextFreeLocalVlanIndex_Type())
fsDot1qNextFreeLocalVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qNextFreeLocalVlanIndex.setStatus(_A)
_FsDot1qPortVlanTable_Object=MibTable
fsDot1qPortVlanTable=_FsDot1qPortVlanTable_Object((1,3,6,1,4,1,2076,116,7,1,4,7))
if mibBuilder.loadTexts:fsDot1qPortVlanTable.setStatus(_A)
_FsDot1qPortVlanEntry_Object=MibTableRow
fsDot1qPortVlanEntry=_FsDot1qPortVlanEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1))
fsDot1qPortVlanEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:fsDot1qPortVlanEntry.setStatus(_A)
class _FsDot1qPvid_Type(VlanIndex):defaultValue=1
_FsDot1qPvid_Type.__name__=_h
_FsDot1qPvid_Object=MibTableColumn
fsDot1qPvid=_FsDot1qPvid_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,1),_FsDot1qPvid_Type())
fsDot1qPvid.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qPvid.setStatus(_A)
class _FsDot1qPortAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2),('admitOnlyUntaggedAndPriorityTagged',3)))
_FsDot1qPortAcceptableFrameTypes_Type.__name__=_D
_FsDot1qPortAcceptableFrameTypes_Object=MibTableColumn
fsDot1qPortAcceptableFrameTypes=_FsDot1qPortAcceptableFrameTypes_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,2),_FsDot1qPortAcceptableFrameTypes_Type())
fsDot1qPortAcceptableFrameTypes.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qPortAcceptableFrameTypes.setStatus(_A)
class _FsDot1qPortIngressFiltering_Type(TruthValue):defaultValue=2
_FsDot1qPortIngressFiltering_Type.__name__=_Q
_FsDot1qPortIngressFiltering_Object=MibTableColumn
fsDot1qPortIngressFiltering=_FsDot1qPortIngressFiltering_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,3),_FsDot1qPortIngressFiltering_Type())
fsDot1qPortIngressFiltering.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qPortIngressFiltering.setStatus(_A)
class _FsDot1qPortGvrpStatus_Type(EnabledStatus):defaultValue=1
_FsDot1qPortGvrpStatus_Type.__name__=_b
_FsDot1qPortGvrpStatus_Object=MibTableColumn
fsDot1qPortGvrpStatus=_FsDot1qPortGvrpStatus_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,4),_FsDot1qPortGvrpStatus_Type())
fsDot1qPortGvrpStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qPortGvrpStatus.setStatus(_A)
_FsDot1qPortGvrpFailedRegistrations_Type=Counter32
_FsDot1qPortGvrpFailedRegistrations_Object=MibTableColumn
fsDot1qPortGvrpFailedRegistrations=_FsDot1qPortGvrpFailedRegistrations_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,5),_FsDot1qPortGvrpFailedRegistrations_Type())
fsDot1qPortGvrpFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qPortGvrpFailedRegistrations.setStatus(_A)
_FsDot1qPortGvrpLastPduOrigin_Type=MacAddress
_FsDot1qPortGvrpLastPduOrigin_Object=MibTableColumn
fsDot1qPortGvrpLastPduOrigin=_FsDot1qPortGvrpLastPduOrigin_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,6),_FsDot1qPortGvrpLastPduOrigin_Type())
fsDot1qPortGvrpLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qPortGvrpLastPduOrigin.setStatus(_A)
class _FsDot1qPortRestrictedVlanRegistration_Type(TruthValue):defaultValue=2
_FsDot1qPortRestrictedVlanRegistration_Type.__name__=_Q
_FsDot1qPortRestrictedVlanRegistration_Object=MibTableColumn
fsDot1qPortRestrictedVlanRegistration=_FsDot1qPortRestrictedVlanRegistration_Object((1,3,6,1,4,1,2076,116,7,1,4,7,1,7),_FsDot1qPortRestrictedVlanRegistration_Type())
fsDot1qPortRestrictedVlanRegistration.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qPortRestrictedVlanRegistration.setStatus(_A)
_FsDot1qPortVlanStatisticsTable_Object=MibTable
fsDot1qPortVlanStatisticsTable=_FsDot1qPortVlanStatisticsTable_Object((1,3,6,1,4,1,2076,116,7,1,4,8))
if mibBuilder.loadTexts:fsDot1qPortVlanStatisticsTable.setStatus(_A)
_FsDot1qPortVlanStatisticsEntry_Object=MibTableRow
fsDot1qPortVlanStatisticsEntry=_FsDot1qPortVlanStatisticsEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1))
fsDot1qPortVlanStatisticsEntry.setIndexNames((0,_K,_L),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qPortVlanStatisticsEntry.setStatus(_A)
_FsDot1qTpVlanPortInFrames_Type=Counter32
_FsDot1qTpVlanPortInFrames_Object=MibTableColumn
fsDot1qTpVlanPortInFrames=_FsDot1qTpVlanPortInFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,1),_FsDot1qTpVlanPortInFrames_Type())
fsDot1qTpVlanPortInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortInFrames.setStatus(_A)
_FsDot1qTpVlanPortOutFrames_Type=Counter32
_FsDot1qTpVlanPortOutFrames_Object=MibTableColumn
fsDot1qTpVlanPortOutFrames=_FsDot1qTpVlanPortOutFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,2),_FsDot1qTpVlanPortOutFrames_Type())
fsDot1qTpVlanPortOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortOutFrames.setStatus(_A)
_FsDot1qTpVlanPortInDiscards_Type=Counter32
_FsDot1qTpVlanPortInDiscards_Object=MibTableColumn
fsDot1qTpVlanPortInDiscards=_FsDot1qTpVlanPortInDiscards_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,3),_FsDot1qTpVlanPortInDiscards_Type())
fsDot1qTpVlanPortInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortInDiscards.setStatus(_A)
_FsDot1qTpVlanPortInOverflowFrames_Type=Counter32
_FsDot1qTpVlanPortInOverflowFrames_Object=MibTableColumn
fsDot1qTpVlanPortInOverflowFrames=_FsDot1qTpVlanPortInOverflowFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,4),_FsDot1qTpVlanPortInOverflowFrames_Type())
fsDot1qTpVlanPortInOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortInOverflowFrames.setStatus(_A)
_FsDot1qTpVlanPortOutOverflowFrames_Type=Counter32
_FsDot1qTpVlanPortOutOverflowFrames_Object=MibTableColumn
fsDot1qTpVlanPortOutOverflowFrames=_FsDot1qTpVlanPortOutOverflowFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,5),_FsDot1qTpVlanPortOutOverflowFrames_Type())
fsDot1qTpVlanPortOutOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortOutOverflowFrames.setStatus(_A)
_FsDot1qTpVlanPortInOverflowDiscards_Type=Counter32
_FsDot1qTpVlanPortInOverflowDiscards_Object=MibTableColumn
fsDot1qTpVlanPortInOverflowDiscards=_FsDot1qTpVlanPortInOverflowDiscards_Object((1,3,6,1,4,1,2076,116,7,1,4,8,1,6),_FsDot1qTpVlanPortInOverflowDiscards_Type())
fsDot1qTpVlanPortInOverflowDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortInOverflowDiscards.setStatus(_A)
_FsDot1qPortVlanHCStatisticsTable_Object=MibTable
fsDot1qPortVlanHCStatisticsTable=_FsDot1qPortVlanHCStatisticsTable_Object((1,3,6,1,4,1,2076,116,7,1,4,9))
if mibBuilder.loadTexts:fsDot1qPortVlanHCStatisticsTable.setStatus(_A)
_FsDot1qPortVlanHCStatisticsEntry_Object=MibTableRow
fsDot1qPortVlanHCStatisticsEntry=_FsDot1qPortVlanHCStatisticsEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,9,1))
fsDot1qPortVlanHCStatisticsEntry.setIndexNames((0,_K,_L),(0,_B,_G))
if mibBuilder.loadTexts:fsDot1qPortVlanHCStatisticsEntry.setStatus(_A)
_FsDot1qTpVlanPortHCInFrames_Type=Counter64
_FsDot1qTpVlanPortHCInFrames_Object=MibTableColumn
fsDot1qTpVlanPortHCInFrames=_FsDot1qTpVlanPortHCInFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,9,1,1),_FsDot1qTpVlanPortHCInFrames_Type())
fsDot1qTpVlanPortHCInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortHCInFrames.setStatus(_A)
_FsDot1qTpVlanPortHCOutFrames_Type=Counter64
_FsDot1qTpVlanPortHCOutFrames_Object=MibTableColumn
fsDot1qTpVlanPortHCOutFrames=_FsDot1qTpVlanPortHCOutFrames_Object((1,3,6,1,4,1,2076,116,7,1,4,9,1,2),_FsDot1qTpVlanPortHCOutFrames_Type())
fsDot1qTpVlanPortHCOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortHCOutFrames.setStatus(_A)
_FsDot1qTpVlanPortHCInDiscards_Type=Counter64
_FsDot1qTpVlanPortHCInDiscards_Object=MibTableColumn
fsDot1qTpVlanPortHCInDiscards=_FsDot1qTpVlanPortHCInDiscards_Object((1,3,6,1,4,1,2076,116,7,1,4,9,1,3),_FsDot1qTpVlanPortHCInDiscards_Type())
fsDot1qTpVlanPortHCInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot1qTpVlanPortHCInDiscards.setStatus(_A)
_FsDot1qLearningConstraintsTable_Object=MibTable
fsDot1qLearningConstraintsTable=_FsDot1qLearningConstraintsTable_Object((1,3,6,1,4,1,2076,116,7,1,4,10))
if mibBuilder.loadTexts:fsDot1qLearningConstraintsTable.setStatus(_A)
_FsDot1qLearningConstraintsEntry_Object=MibTableRow
fsDot1qLearningConstraintsEntry=_FsDot1qLearningConstraintsEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,10,1))
fsDot1qLearningConstraintsEntry.setIndexNames((0,_B,_E),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:fsDot1qLearningConstraintsEntry.setStatus(_A)
_FsDot1qConstraintVlan_Type=VlanIndex
_FsDot1qConstraintVlan_Object=MibTableColumn
fsDot1qConstraintVlan=_FsDot1qConstraintVlan_Object((1,3,6,1,4,1,2076,116,7,1,4,10,1,1),_FsDot1qConstraintVlan_Type())
fsDot1qConstraintVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qConstraintVlan.setStatus(_A)
class _FsDot1qConstraintSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qConstraintSet_Type.__name__=_D
_FsDot1qConstraintSet_Object=MibTableColumn
fsDot1qConstraintSet=_FsDot1qConstraintSet_Object((1,3,6,1,4,1,2076,116,7,1,4,10,1,2),_FsDot1qConstraintSet_Type())
fsDot1qConstraintSet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1qConstraintSet.setStatus(_A)
class _FsDot1qConstraintType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_FsDot1qConstraintType_Type.__name__=_D
_FsDot1qConstraintType_Object=MibTableColumn
fsDot1qConstraintType=_FsDot1qConstraintType_Object((1,3,6,1,4,1,2076,116,7,1,4,10,1,3),_FsDot1qConstraintType_Type())
fsDot1qConstraintType.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qConstraintType.setStatus(_A)
_FsDot1qConstraintStatus_Type=RowStatus
_FsDot1qConstraintStatus_Object=MibTableColumn
fsDot1qConstraintStatus=_FsDot1qConstraintStatus_Object((1,3,6,1,4,1,2076,116,7,1,4,10,1,4),_FsDot1qConstraintStatus_Type())
fsDot1qConstraintStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1qConstraintStatus.setStatus(_A)
_FsDot1qConstraintDefaultTable_Object=MibTable
fsDot1qConstraintDefaultTable=_FsDot1qConstraintDefaultTable_Object((1,3,6,1,4,1,2076,116,7,1,4,11))
if mibBuilder.loadTexts:fsDot1qConstraintDefaultTable.setStatus(_A)
_FsDot1qConstraintDefaultEntry_Object=MibTableRow
fsDot1qConstraintDefaultEntry=_FsDot1qConstraintDefaultEntry_Object((1,3,6,1,4,1,2076,116,7,1,4,11,1))
fsDot1qConstraintDefaultEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsDot1qConstraintDefaultEntry.setStatus(_A)
class _FsDot1qConstraintSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1qConstraintSetDefault_Type.__name__=_D
_FsDot1qConstraintSetDefault_Object=MibTableColumn
fsDot1qConstraintSetDefault=_FsDot1qConstraintSetDefault_Object((1,3,6,1,4,1,2076,116,7,1,4,11,1,1),_FsDot1qConstraintSetDefault_Type())
fsDot1qConstraintSetDefault.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qConstraintSetDefault.setStatus(_A)
class _FsDot1qConstraintTypeDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_FsDot1qConstraintTypeDefault_Type.__name__=_D
_FsDot1qConstraintTypeDefault_Object=MibTableColumn
fsDot1qConstraintTypeDefault=_FsDot1qConstraintTypeDefault_Object((1,3,6,1,4,1,2076,116,7,1,4,11,1,2),_FsDot1qConstraintTypeDefault_Type())
fsDot1qConstraintTypeDefault.setMaxAccess(_H)
if mibBuilder.loadTexts:fsDot1qConstraintTypeDefault.setStatus(_A)
_FsDot1vProtocol_ObjectIdentity=ObjectIdentity
fsDot1vProtocol=_FsDot1vProtocol_ObjectIdentity((1,3,6,1,4,1,2076,116,7,1,5))
_FsDot1vProtocolGroupTable_Object=MibTable
fsDot1vProtocolGroupTable=_FsDot1vProtocolGroupTable_Object((1,3,6,1,4,1,2076,116,7,1,5,1))
if mibBuilder.loadTexts:fsDot1vProtocolGroupTable.setStatus(_A)
_FsDot1vProtocolGroupEntry_Object=MibTableRow
fsDot1vProtocolGroupEntry=_FsDot1vProtocolGroupEntry_Object((1,3,6,1,4,1,2076,116,7,1,5,1,1))
fsDot1vProtocolGroupEntry.setIndexNames((0,_B,_E),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:fsDot1vProtocolGroupEntry.setStatus(_A)
class _FsDot1vProtocolTemplateFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ethernet',1),('rfc1042',2),('snap8021H',3),('snapOther',4),('llcOther',5)))
_FsDot1vProtocolTemplateFrameType_Type.__name__=_D
_FsDot1vProtocolTemplateFrameType_Object=MibTableColumn
fsDot1vProtocolTemplateFrameType=_FsDot1vProtocolTemplateFrameType_Object((1,3,6,1,4,1,2076,116,7,1,5,1,1,1),_FsDot1vProtocolTemplateFrameType_Type())
fsDot1vProtocolTemplateFrameType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1vProtocolTemplateFrameType.setStatus(_A)
class _FsDot1vProtocolTemplateProtocolValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2),ValueSizeConstraint(5,5))
_FsDot1vProtocolTemplateProtocolValue_Type.__name__=_a
_FsDot1vProtocolTemplateProtocolValue_Object=MibTableColumn
fsDot1vProtocolTemplateProtocolValue=_FsDot1vProtocolTemplateProtocolValue_Object((1,3,6,1,4,1,2076,116,7,1,5,1,1,2),_FsDot1vProtocolTemplateProtocolValue_Type())
fsDot1vProtocolTemplateProtocolValue.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1vProtocolTemplateProtocolValue.setStatus(_A)
class _FsDot1vProtocolGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsDot1vProtocolGroupId_Type.__name__=_D
_FsDot1vProtocolGroupId_Object=MibTableColumn
fsDot1vProtocolGroupId=_FsDot1vProtocolGroupId_Object((1,3,6,1,4,1,2076,116,7,1,5,1,1,3),_FsDot1vProtocolGroupId_Type())
fsDot1vProtocolGroupId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1vProtocolGroupId.setStatus(_A)
_FsDot1vProtocolGroupRowStatus_Type=RowStatus
_FsDot1vProtocolGroupRowStatus_Object=MibTableColumn
fsDot1vProtocolGroupRowStatus=_FsDot1vProtocolGroupRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,5,1,1,4),_FsDot1vProtocolGroupRowStatus_Type())
fsDot1vProtocolGroupRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1vProtocolGroupRowStatus.setStatus(_A)
_FsDot1vProtocolPortTable_Object=MibTable
fsDot1vProtocolPortTable=_FsDot1vProtocolPortTable_Object((1,3,6,1,4,1,2076,116,7,1,5,2))
if mibBuilder.loadTexts:fsDot1vProtocolPortTable.setStatus(_A)
_FsDot1vProtocolPortEntry_Object=MibTableRow
fsDot1vProtocolPortEntry=_FsDot1vProtocolPortEntry_Object((1,3,6,1,4,1,2076,116,7,1,5,2,1))
fsDot1vProtocolPortEntry.setIndexNames((0,_K,_L),(0,_B,_o))
if mibBuilder.loadTexts:fsDot1vProtocolPortEntry.setStatus(_A)
class _FsDot1vProtocolPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDot1vProtocolPortGroupId_Type.__name__=_D
_FsDot1vProtocolPortGroupId_Object=MibTableColumn
fsDot1vProtocolPortGroupId=_FsDot1vProtocolPortGroupId_Object((1,3,6,1,4,1,2076,116,7,1,5,2,1,1),_FsDot1vProtocolPortGroupId_Type())
fsDot1vProtocolPortGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1vProtocolPortGroupId.setStatus(_A)
class _FsDot1vProtocolPortGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsDot1vProtocolPortGroupVid_Type.__name__=_D
_FsDot1vProtocolPortGroupVid_Object=MibTableColumn
fsDot1vProtocolPortGroupVid=_FsDot1vProtocolPortGroupVid_Object((1,3,6,1,4,1,2076,116,7,1,5,2,1,2),_FsDot1vProtocolPortGroupVid_Type())
fsDot1vProtocolPortGroupVid.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1vProtocolPortGroupVid.setStatus(_A)
_FsDot1vProtocolPortRowStatus_Type=RowStatus
_FsDot1vProtocolPortRowStatus_Object=MibTableColumn
fsDot1vProtocolPortRowStatus=_FsDot1vProtocolPortRowStatus_Object((1,3,6,1,4,1,2076,116,7,1,5,2,1,3),_FsDot1vProtocolPortRowStatus_Type())
fsDot1vProtocolPortRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsDot1vProtocolPortRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_h:VlanIndex,'VlanId':VlanId,'fsQBridgeMIB':fsQBridgeMIB,'fsQBridgeMIBObjects':fsQBridgeMIBObjects,'fsDot1qBase':fsDot1qBase,'fsDot1qBaseTable':fsDot1qBaseTable,'fsDot1qBaseEntry':fsDot1qBaseEntry,_E:fsDot1qVlanContextId,'fsDot1qVlanVersionNumber':fsDot1qVlanVersionNumber,'fsDot1qMaxVlanId':fsDot1qMaxVlanId,'fsDot1qMaxSupportedVlans':fsDot1qMaxSupportedVlans,'fsDot1qNumVlans':fsDot1qNumVlans,'fsDot1qGvrpStatus':fsDot1qGvrpStatus,'fsDot1qTp':fsDot1qTp,'fsDot1qFdbTable':fsDot1qFdbTable,'fsDot1qFdbEntry':fsDot1qFdbEntry,_M:fsDot1qFdbId,'fsDot1qFdbDynamicCount':fsDot1qFdbDynamicCount,'fsDot1qTpFdbTable':fsDot1qTpFdbTable,'fsDot1qTpFdbEntry':fsDot1qTpFdbEntry,_d:fsDot1qTpFdbAddress,'fsDot1qTpFdbPort':fsDot1qTpFdbPort,'fsDot1qTpFdbStatus':fsDot1qTpFdbStatus,'fsDot1qTpFdbPw':fsDot1qTpFdbPw,'fsDot1qTpGroupTable':fsDot1qTpGroupTable,'fsDot1qTpGroupEntry':fsDot1qTpGroupEntry,_G:fsDot1qVlanIndex,_e:fsDot1qTpGroupAddress,_J:fsDot1qTpPort,'fsDot1qTpGroupIsLearnt':fsDot1qTpGroupIsLearnt,'fsDot1qForwardAllLearntPortTable':fsDot1qForwardAllLearntPortTable,'fsDot1qForwardAllLearntPortEntry':fsDot1qForwardAllLearntPortEntry,'fsDot1qForwardAllIsLearnt':fsDot1qForwardAllIsLearnt,'fsDot1qForwardAllStatusTable':fsDot1qForwardAllStatusTable,'fsDot1qForwardAllStatusEntry':fsDot1qForwardAllStatusEntry,'fsDot1qForwardAllRowStatus':fsDot1qForwardAllRowStatus,'fsDot1qForwardAllPortConfigTable':fsDot1qForwardAllPortConfigTable,'fsDot1qForwardAllPortConfigEntry':fsDot1qForwardAllPortConfigEntry,'fsDot1qForwardAllPort':fsDot1qForwardAllPort,'fsDot1qForwardUnregLearntPortTable':fsDot1qForwardUnregLearntPortTable,'fsDot1qForwardUnregLearntPortEntry':fsDot1qForwardUnregLearntPortEntry,'fsDot1qForwardUnregIsLearnt':fsDot1qForwardUnregIsLearnt,'fsDot1qForwardUnregStatusTable':fsDot1qForwardUnregStatusTable,'fsDot1qForwardUnregStatusEntry':fsDot1qForwardUnregStatusEntry,'fsDot1qForwardUnregRowStatus':fsDot1qForwardUnregRowStatus,'fsDot1qForwardUnregPortConfigTable':fsDot1qForwardUnregPortConfigTable,'fsDot1qForwardUnregPortConfigEntry':fsDot1qForwardUnregPortConfigEntry,'fsDot1qForwardUnregPort':fsDot1qForwardUnregPort,'fsDot1qStatic':fsDot1qStatic,'fsDot1qStaticUnicastTable':fsDot1qStaticUnicastTable,'fsDot1qStaticUnicastEntry':fsDot1qStaticUnicastEntry,_U:fsDot1qStaticUnicastAddress,_V:fsDot1qStaticUnicastReceivePort,'fsDot1qStaticUnicastRowStatus':fsDot1qStaticUnicastRowStatus,'fsDot1qStaticUnicastStatus':fsDot1qStaticUnicastStatus,'fsDot1qStaticAllowedToGoTable':fsDot1qStaticAllowedToGoTable,'fsDot1qStaticAllowedToGoEntry':fsDot1qStaticAllowedToGoEntry,'fsDot1qStaticAllowedIsMember':fsDot1qStaticAllowedIsMember,'fsDot1qStaticMulticastTable':fsDot1qStaticMulticastTable,'fsDot1qStaticMulticastEntry':fsDot1qStaticMulticastEntry,_X:fsDot1qStaticMulticastAddress,_Y:fsDot1qStaticMulticastReceivePort,'fsDot1qStaticMulticastRowStatus':fsDot1qStaticMulticastRowStatus,'fsDot1qStaticMulticastStatus':fsDot1qStaticMulticastStatus,'fsDot1qStaticMcastPortTable':fsDot1qStaticMcastPortTable,'fsDot1qStaticMcastPortEntry':fsDot1qStaticMcastPortEntry,'fsDot1qStaticMcastPort':fsDot1qStaticMcastPort,'fsDot1qVlan':fsDot1qVlan,'fsDot1qVlanNumDeletesTable':fsDot1qVlanNumDeletesTable,'fsDot1qVlanNumDeletesEntry':fsDot1qVlanNumDeletesEntry,'fsDot1qVlanNumDeletes':fsDot1qVlanNumDeletes,'fsDot1qVlanCurrentTable':fsDot1qVlanCurrentTable,'fsDot1qVlanCurrentEntry':fsDot1qVlanCurrentEntry,_Z:fsDot1qVlanTimeMark,'fsDot1qVlanFdbId':fsDot1qVlanFdbId,'fsDot1qVlanStatus':fsDot1qVlanStatus,'fsDot1qVlanCreationTime':fsDot1qVlanCreationTime,'fsDot1qVlanEgressPortTable':fsDot1qVlanEgressPortTable,'fsDot1qVlanEgressPortEntry':fsDot1qVlanEgressPortEntry,'fsDot1qVlanCurrentEgressPort':fsDot1qVlanCurrentEgressPort,'fsDot1qVlanStaticTable':fsDot1qVlanStaticTable,'fsDot1qVlanStaticEntry':fsDot1qVlanStaticEntry,'fsDot1qVlanStaticName':fsDot1qVlanStaticName,'fsDot1qVlanStaticRowStatus':fsDot1qVlanStaticRowStatus,'fsDot1qVlanStaticPortConfigTable':fsDot1qVlanStaticPortConfigTable,'fsDot1qVlanStaticPortConfigEntry':fsDot1qVlanStaticPortConfigEntry,'fsDot1qVlanStaticPort':fsDot1qVlanStaticPort,'fsDot1qNextFreeLocalVlanIndexTable':fsDot1qNextFreeLocalVlanIndexTable,'fsDot1qNextFreeLocalVlanIndexEntry':fsDot1qNextFreeLocalVlanIndexEntry,'fsDot1qNextFreeLocalVlanIndex':fsDot1qNextFreeLocalVlanIndex,'fsDot1qPortVlanTable':fsDot1qPortVlanTable,'fsDot1qPortVlanEntry':fsDot1qPortVlanEntry,'fsDot1qPvid':fsDot1qPvid,'fsDot1qPortAcceptableFrameTypes':fsDot1qPortAcceptableFrameTypes,'fsDot1qPortIngressFiltering':fsDot1qPortIngressFiltering,'fsDot1qPortGvrpStatus':fsDot1qPortGvrpStatus,'fsDot1qPortGvrpFailedRegistrations':fsDot1qPortGvrpFailedRegistrations,'fsDot1qPortGvrpLastPduOrigin':fsDot1qPortGvrpLastPduOrigin,'fsDot1qPortRestrictedVlanRegistration':fsDot1qPortRestrictedVlanRegistration,'fsDot1qPortVlanStatisticsTable':fsDot1qPortVlanStatisticsTable,'fsDot1qPortVlanStatisticsEntry':fsDot1qPortVlanStatisticsEntry,'fsDot1qTpVlanPortInFrames':fsDot1qTpVlanPortInFrames,'fsDot1qTpVlanPortOutFrames':fsDot1qTpVlanPortOutFrames,'fsDot1qTpVlanPortInDiscards':fsDot1qTpVlanPortInDiscards,'fsDot1qTpVlanPortInOverflowFrames':fsDot1qTpVlanPortInOverflowFrames,'fsDot1qTpVlanPortOutOverflowFrames':fsDot1qTpVlanPortOutOverflowFrames,'fsDot1qTpVlanPortInOverflowDiscards':fsDot1qTpVlanPortInOverflowDiscards,'fsDot1qPortVlanHCStatisticsTable':fsDot1qPortVlanHCStatisticsTable,'fsDot1qPortVlanHCStatisticsEntry':fsDot1qPortVlanHCStatisticsEntry,'fsDot1qTpVlanPortHCInFrames':fsDot1qTpVlanPortHCInFrames,'fsDot1qTpVlanPortHCOutFrames':fsDot1qTpVlanPortHCOutFrames,'fsDot1qTpVlanPortHCInDiscards':fsDot1qTpVlanPortHCInDiscards,'fsDot1qLearningConstraintsTable':fsDot1qLearningConstraintsTable,'fsDot1qLearningConstraintsEntry':fsDot1qLearningConstraintsEntry,_i:fsDot1qConstraintVlan,_j:fsDot1qConstraintSet,'fsDot1qConstraintType':fsDot1qConstraintType,'fsDot1qConstraintStatus':fsDot1qConstraintStatus,'fsDot1qConstraintDefaultTable':fsDot1qConstraintDefaultTable,'fsDot1qConstraintDefaultEntry':fsDot1qConstraintDefaultEntry,'fsDot1qConstraintSetDefault':fsDot1qConstraintSetDefault,'fsDot1qConstraintTypeDefault':fsDot1qConstraintTypeDefault,'fsDot1vProtocol':fsDot1vProtocol,'fsDot1vProtocolGroupTable':fsDot1vProtocolGroupTable,'fsDot1vProtocolGroupEntry':fsDot1vProtocolGroupEntry,_m:fsDot1vProtocolTemplateFrameType,_n:fsDot1vProtocolTemplateProtocolValue,'fsDot1vProtocolGroupId':fsDot1vProtocolGroupId,'fsDot1vProtocolGroupRowStatus':fsDot1vProtocolGroupRowStatus,'fsDot1vProtocolPortTable':fsDot1vProtocolPortTable,'fsDot1vProtocolPortEntry':fsDot1vProtocolPortEntry,_o:fsDot1vProtocolPortGroupId,'fsDot1vProtocolPortGroupVid':fsDot1vProtocolPortGroupVid,'fsDot1vProtocolPortRowStatus':fsDot1vProtocolPortRowStatus})