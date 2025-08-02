_V='percentage'
_U='extremeIQosProfileIndex'
_T='extremeQosIngressPriorityIndex'
_S='extremePerPortQosIndex'
_R='highHi'
_Q='mediumHi'
_P='medium'
_O='normalHi'
_N='normal'
_M='extremeQosProfileIndex'
_L='deprecated'
_K='ifIndex'
_J='IF-MIB'
_I='extremeVlanIfIndex'
_H='EXTREME-VLAN-MIB'
_G='read-write'
_F='DisplayString'
_E='EXTREME-QOS-MIB'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
extremeVlanIfIndex,=mibBuilder.importSymbols(_H,_I)
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeQos=ModuleIdentity((1,3,6,1,4,1,1916,1,3))
_ExtremeQosCommon_ObjectIdentity=ObjectIdentity
extremeQosCommon=_ExtremeQosCommon_ObjectIdentity((1,3,6,1,4,1,1916,1,3,1))
class _ExtremeUnitPaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('normalEthernet',2),('lowLatency',3)))
_ExtremeUnitPaceMode_Type.__name__=_B
_ExtremeUnitPaceMode_Object=MibScalar
extremeUnitPaceMode=_ExtremeUnitPaceMode_Object((1,3,6,1,4,1,1916,1,3,1,1),_ExtremeUnitPaceMode_Type())
extremeUnitPaceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeUnitPaceMode.setStatus(_L)
class _ExtremeQosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_ExtremeQosMode_Type.__name__=_B
_ExtremeQosMode_Object=MibScalar
extremeQosMode=_ExtremeQosMode_Object((1,3,6,1,4,1,1916,1,3,1,4),_ExtremeQosMode_Type())
extremeQosMode.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeQosMode.setStatus(_L)
_ExtremeQosUnconfigure_Type=TruthValue
_ExtremeQosUnconfigure_Object=MibScalar
extremeQosUnconfigure=_ExtremeQosUnconfigure_Object((1,3,6,1,4,1,1916,1,3,1,5),_ExtremeQosUnconfigure_Type())
extremeQosUnconfigure.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeQosUnconfigure.setStatus(_L)
_ExtremeQosProfileTable_Object=MibTable
extremeQosProfileTable=_ExtremeQosProfileTable_Object((1,3,6,1,4,1,1916,1,3,1,6))
if mibBuilder.loadTexts:extremeQosProfileTable.setStatus(_A)
_ExtremeQosProfileEntry_Object=MibTableRow
extremeQosProfileEntry=_ExtremeQosProfileEntry_Object((1,3,6,1,4,1,1916,1,3,1,6,1))
extremeQosProfileEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:extremeQosProfileEntry.setStatus(_A)
class _ExtremeQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeQosProfileIndex_Type.__name__=_B
_ExtremeQosProfileIndex_Object=MibTableColumn
extremeQosProfileIndex=_ExtremeQosProfileIndex_Object((1,3,6,1,4,1,1916,1,3,1,6,1,1),_ExtremeQosProfileIndex_Type())
extremeQosProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfileIndex.setStatus(_A)
class _ExtremeQosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeQosProfileName_Type.__name__=_F
_ExtremeQosProfileName_Object=MibTableColumn
extremeQosProfileName=_ExtremeQosProfileName_Object((1,3,6,1,4,1,1916,1,3,1,6,1,2),_ExtremeQosProfileName_Type())
extremeQosProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfileName.setStatus(_A)
class _ExtremeQosProfileMinBw_Type(Integer32):defaultValue=0
_ExtremeQosProfileMinBw_Type.__name__=_B
_ExtremeQosProfileMinBw_Object=MibTableColumn
extremeQosProfileMinBw=_ExtremeQosProfileMinBw_Object((1,3,6,1,4,1,1916,1,3,1,6,1,3),_ExtremeQosProfileMinBw_Type())
extremeQosProfileMinBw.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfileMinBw.setStatus(_A)
class _ExtremeQosProfileMaxBw_Type(Integer32):defaultValue=100
_ExtremeQosProfileMaxBw_Type.__name__=_B
_ExtremeQosProfileMaxBw_Object=MibTableColumn
extremeQosProfileMaxBw=_ExtremeQosProfileMaxBw_Object((1,3,6,1,4,1,1916,1,3,1,6,1,4),_ExtremeQosProfileMaxBw_Type())
extremeQosProfileMaxBw.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfileMaxBw.setStatus(_A)
class _ExtremeQosProfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('low',1),('lowHi',2),(_N,3),(_O,4),(_P,5),(_Q,6),('high',7),(_R,8)))
_ExtremeQosProfilePriority_Type.__name__=_B
_ExtremeQosProfilePriority_Object=MibTableColumn
extremeQosProfilePriority=_ExtremeQosProfilePriority_Object((1,3,6,1,4,1,1916,1,3,1,6,1,5),_ExtremeQosProfilePriority_Type())
extremeQosProfilePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfilePriority.setStatus(_A)
_ExtremeQosProfileRowStatus_Type=RowStatus
_ExtremeQosProfileRowStatus_Object=MibTableColumn
extremeQosProfileRowStatus=_ExtremeQosProfileRowStatus_Object((1,3,6,1,4,1,1916,1,3,1,6,1,6),_ExtremeQosProfileRowStatus_Type())
extremeQosProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeQosProfileRowStatus.setStatus(_A)
_ExtremeQosByVlanMappingTable_Object=MibTable
extremeQosByVlanMappingTable=_ExtremeQosByVlanMappingTable_Object((1,3,6,1,4,1,1916,1,3,1,7))
if mibBuilder.loadTexts:extremeQosByVlanMappingTable.setStatus(_A)
_ExtremeQosByVlanMappingEntry_Object=MibTableRow
extremeQosByVlanMappingEntry=_ExtremeQosByVlanMappingEntry_Object((1,3,6,1,4,1,1916,1,3,1,7,1))
extremeQosByVlanMappingEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:extremeQosByVlanMappingEntry.setStatus(_A)
class _ExtremeQosByVlanMappingQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeQosByVlanMappingQosProfileIndex_Type.__name__=_B
_ExtremeQosByVlanMappingQosProfileIndex_Object=MibTableColumn
extremeQosByVlanMappingQosProfileIndex=_ExtremeQosByVlanMappingQosProfileIndex_Object((1,3,6,1,4,1,1916,1,3,1,7,1,1),_ExtremeQosByVlanMappingQosProfileIndex_Type())
extremeQosByVlanMappingQosProfileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeQosByVlanMappingQosProfileIndex.setStatus(_A)
_ExtremePerPortQosTable_Object=MibTable
extremePerPortQosTable=_ExtremePerPortQosTable_Object((1,3,6,1,4,1,1916,1,3,1,8))
if mibBuilder.loadTexts:extremePerPortQosTable.setStatus(_A)
_ExtremePerPortQosEntry_Object=MibTableRow
extremePerPortQosEntry=_ExtremePerPortQosEntry_Object((1,3,6,1,4,1,1916,1,3,1,8,1))
extremePerPortQosEntry.setIndexNames((0,_J,_K),(0,_E,_S))
if mibBuilder.loadTexts:extremePerPortQosEntry.setStatus(_A)
class _ExtremePerPortQosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremePerPortQosIndex_Type.__name__=_B
_ExtremePerPortQosIndex_Object=MibTableColumn
extremePerPortQosIndex=_ExtremePerPortQosIndex_Object((1,3,6,1,4,1,1916,1,3,1,8,1,1),_ExtremePerPortQosIndex_Type())
extremePerPortQosIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePerPortQosIndex.setStatus(_A)
class _ExtremePerPortQosMinBw_Type(Integer32):defaultValue=0
_ExtremePerPortQosMinBw_Type.__name__=_B
_ExtremePerPortQosMinBw_Object=MibTableColumn
extremePerPortQosMinBw=_ExtremePerPortQosMinBw_Object((1,3,6,1,4,1,1916,1,3,1,8,1,2),_ExtremePerPortQosMinBw_Type())
extremePerPortQosMinBw.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePerPortQosMinBw.setStatus(_A)
class _ExtremePerPortQosMaxBw_Type(Integer32):defaultValue=100
_ExtremePerPortQosMaxBw_Type.__name__=_B
_ExtremePerPortQosMaxBw_Object=MibTableColumn
extremePerPortQosMaxBw=_ExtremePerPortQosMaxBw_Object((1,3,6,1,4,1,1916,1,3,1,8,1,3),_ExtremePerPortQosMaxBw_Type())
extremePerPortQosMaxBw.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePerPortQosMaxBw.setStatus(_A)
class _ExtremePerPortQosPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('low',1),('lowHi',2),(_N,3),(_O,4),(_P,5),(_Q,6),('high',7),(_R,8)))
_ExtremePerPortQosPriority_Type.__name__=_B
_ExtremePerPortQosPriority_Object=MibTableColumn
extremePerPortQosPriority=_ExtremePerPortQosPriority_Object((1,3,6,1,4,1,1916,1,3,1,8,1,4),_ExtremePerPortQosPriority_Type())
extremePerPortQosPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePerPortQosPriority.setStatus(_A)
_ExtremePerPortQosRowStatus_Type=RowStatus
_ExtremePerPortQosRowStatus_Object=MibTableColumn
extremePerPortQosRowStatus=_ExtremePerPortQosRowStatus_Object((1,3,6,1,4,1,1916,1,3,1,8,1,5),_ExtremePerPortQosRowStatus_Type())
extremePerPortQosRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePerPortQosRowStatus.setStatus(_A)
_ExtremeQosIngressPriorityTable_Object=MibTable
extremeQosIngressPriorityTable=_ExtremeQosIngressPriorityTable_Object((1,3,6,1,4,1,1916,1,3,1,9))
if mibBuilder.loadTexts:extremeQosIngressPriorityTable.setStatus(_A)
_ExtremeQosIngressPriorityEntry_Object=MibTableRow
extremeQosIngressPriorityEntry=_ExtremeQosIngressPriorityEntry_Object((1,3,6,1,4,1,1916,1,3,1,9,1))
extremeQosIngressPriorityEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:extremeQosIngressPriorityEntry.setStatus(_A)
class _ExtremeQosIngressPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeQosIngressPriorityIndex_Type.__name__=_B
_ExtremeQosIngressPriorityIndex_Object=MibTableColumn
extremeQosIngressPriorityIndex=_ExtremeQosIngressPriorityIndex_Object((1,3,6,1,4,1,1916,1,3,1,9,1,1),_ExtremeQosIngressPriorityIndex_Type())
extremeQosIngressPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeQosIngressPriorityIndex.setStatus(_A)
class _ExtremeQosIngressPriorityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ExtremeQosIngressPriorityName_Type.__name__=_F
_ExtremeQosIngressPriorityName_Object=MibTableColumn
extremeQosIngressPriorityName=_ExtremeQosIngressPriorityName_Object((1,3,6,1,4,1,1916,1,3,1,9,1,2),_ExtremeQosIngressPriorityName_Type())
extremeQosIngressPriorityName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeQosIngressPriorityName.setStatus(_A)
class _ExtremeQosIngressPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ExtremeQosIngressPriorityValue_Type.__name__=_B
_ExtremeQosIngressPriorityValue_Object=MibTableColumn
extremeQosIngressPriorityValue=_ExtremeQosIngressPriorityValue_Object((1,3,6,1,4,1,1916,1,3,1,9,1,3),_ExtremeQosIngressPriorityValue_Type())
extremeQosIngressPriorityValue.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeQosIngressPriorityValue.setStatus(_A)
_ExtremeIQosProfileTable_Object=MibTable
extremeIQosProfileTable=_ExtremeIQosProfileTable_Object((1,3,6,1,4,1,1916,1,3,1,10))
if mibBuilder.loadTexts:extremeIQosProfileTable.setStatus(_A)
_ExtremeIQosProfileEntry_Object=MibTableRow
extremeIQosProfileEntry=_ExtremeIQosProfileEntry_Object((1,3,6,1,4,1,1916,1,3,1,10,1))
extremeIQosProfileEntry.setIndexNames((0,_J,_K),(0,_E,_U))
if mibBuilder.loadTexts:extremeIQosProfileEntry.setStatus(_A)
class _ExtremeIQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeIQosProfileIndex_Type.__name__=_B
_ExtremeIQosProfileIndex_Object=MibTableColumn
extremeIQosProfileIndex=_ExtremeIQosProfileIndex_Object((1,3,6,1,4,1,1916,1,3,1,10,1,1),_ExtremeIQosProfileIndex_Type())
extremeIQosProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileIndex.setStatus(_A)
class _ExtremeIQosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeIQosProfileName_Type.__name__=_F
_ExtremeIQosProfileName_Object=MibTableColumn
extremeIQosProfileName=_ExtremeIQosProfileName_Object((1,3,6,1,4,1,1916,1,3,1,10,1,2),_ExtremeIQosProfileName_Type())
extremeIQosProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileName.setStatus(_A)
class _ExtremeIQosProfileMinBwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),('kbps',2),('mbps',3)))
_ExtremeIQosProfileMinBwType_Type.__name__=_B
_ExtremeIQosProfileMinBwType_Object=MibTableColumn
extremeIQosProfileMinBwType=_ExtremeIQosProfileMinBwType_Object((1,3,6,1,4,1,1916,1,3,1,10,1,3),_ExtremeIQosProfileMinBwType_Type())
extremeIQosProfileMinBwType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileMinBwType.setStatus(_A)
class _ExtremeIQosProfileMinBw_Type(Integer32):defaultValue=0
_ExtremeIQosProfileMinBw_Type.__name__=_B
_ExtremeIQosProfileMinBw_Object=MibTableColumn
extremeIQosProfileMinBw=_ExtremeIQosProfileMinBw_Object((1,3,6,1,4,1,1916,1,3,1,10,1,4),_ExtremeIQosProfileMinBw_Type())
extremeIQosProfileMinBw.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileMinBw.setStatus(_A)
class _ExtremeIQosProfileMaxBwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),('kbps',2),('mbps',3)))
_ExtremeIQosProfileMaxBwType_Type.__name__=_B
_ExtremeIQosProfileMaxBwType_Object=MibTableColumn
extremeIQosProfileMaxBwType=_ExtremeIQosProfileMaxBwType_Object((1,3,6,1,4,1,1916,1,3,1,10,1,5),_ExtremeIQosProfileMaxBwType_Type())
extremeIQosProfileMaxBwType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileMaxBwType.setStatus(_A)
class _ExtremeIQosProfileMaxBw_Type(Integer32):defaultValue=0
_ExtremeIQosProfileMaxBw_Type.__name__=_B
_ExtremeIQosProfileMaxBw_Object=MibTableColumn
extremeIQosProfileMaxBw=_ExtremeIQosProfileMaxBw_Object((1,3,6,1,4,1,1916,1,3,1,10,1,6),_ExtremeIQosProfileMaxBw_Type())
extremeIQosProfileMaxBw.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileMaxBw.setStatus(_A)
_ExtremeIQosProfileRED_Type=Integer32
_ExtremeIQosProfileRED_Object=MibTableColumn
extremeIQosProfileRED=_ExtremeIQosProfileRED_Object((1,3,6,1,4,1,1916,1,3,1,10,1,7),_ExtremeIQosProfileRED_Type())
extremeIQosProfileRED.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileRED.setStatus(_A)
_ExtremeIQosProfileMaxBuf_Type=Integer32
_ExtremeIQosProfileMaxBuf_Object=MibTableColumn
extremeIQosProfileMaxBuf=_ExtremeIQosProfileMaxBuf_Object((1,3,6,1,4,1,1916,1,3,1,10,1,8),_ExtremeIQosProfileMaxBuf_Type())
extremeIQosProfileMaxBuf.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosProfileMaxBuf.setStatus(_A)
_ExtremeIQosByVlanMappingTable_Object=MibTable
extremeIQosByVlanMappingTable=_ExtremeIQosByVlanMappingTable_Object((1,3,6,1,4,1,1916,1,3,1,11))
if mibBuilder.loadTexts:extremeIQosByVlanMappingTable.setStatus(_A)
_ExtremeIQosByVlanMappingEntry_Object=MibTableRow
extremeIQosByVlanMappingEntry=_ExtremeIQosByVlanMappingEntry_Object((1,3,6,1,4,1,1916,1,3,1,11,1))
extremeIQosByVlanMappingEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:extremeIQosByVlanMappingEntry.setStatus(_A)
class _ExtremeIQosByVlanMappingIQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeIQosByVlanMappingIQosProfileIndex_Type.__name__=_B
_ExtremeIQosByVlanMappingIQosProfileIndex_Object=MibTableColumn
extremeIQosByVlanMappingIQosProfileIndex=_ExtremeIQosByVlanMappingIQosProfileIndex_Object((1,3,6,1,4,1,1916,1,3,1,11,1,1),_ExtremeIQosByVlanMappingIQosProfileIndex_Type())
extremeIQosByVlanMappingIQosProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIQosByVlanMappingIQosProfileIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeQos':extremeQos,'extremeQosCommon':extremeQosCommon,'extremeUnitPaceMode':extremeUnitPaceMode,'extremeQosMode':extremeQosMode,'extremeQosUnconfigure':extremeQosUnconfigure,'extremeQosProfileTable':extremeQosProfileTable,'extremeQosProfileEntry':extremeQosProfileEntry,_M:extremeQosProfileIndex,'extremeQosProfileName':extremeQosProfileName,'extremeQosProfileMinBw':extremeQosProfileMinBw,'extremeQosProfileMaxBw':extremeQosProfileMaxBw,'extremeQosProfilePriority':extremeQosProfilePriority,'extremeQosProfileRowStatus':extremeQosProfileRowStatus,'extremeQosByVlanMappingTable':extremeQosByVlanMappingTable,'extremeQosByVlanMappingEntry':extremeQosByVlanMappingEntry,'extremeQosByVlanMappingQosProfileIndex':extremeQosByVlanMappingQosProfileIndex,'extremePerPortQosTable':extremePerPortQosTable,'extremePerPortQosEntry':extremePerPortQosEntry,_S:extremePerPortQosIndex,'extremePerPortQosMinBw':extremePerPortQosMinBw,'extremePerPortQosMaxBw':extremePerPortQosMaxBw,'extremePerPortQosPriority':extremePerPortQosPriority,'extremePerPortQosRowStatus':extremePerPortQosRowStatus,'extremeQosIngressPriorityTable':extremeQosIngressPriorityTable,'extremeQosIngressPriorityEntry':extremeQosIngressPriorityEntry,_T:extremeQosIngressPriorityIndex,'extremeQosIngressPriorityName':extremeQosIngressPriorityName,'extremeQosIngressPriorityValue':extremeQosIngressPriorityValue,'extremeIQosProfileTable':extremeIQosProfileTable,'extremeIQosProfileEntry':extremeIQosProfileEntry,_U:extremeIQosProfileIndex,'extremeIQosProfileName':extremeIQosProfileName,'extremeIQosProfileMinBwType':extremeIQosProfileMinBwType,'extremeIQosProfileMinBw':extremeIQosProfileMinBw,'extremeIQosProfileMaxBwType':extremeIQosProfileMaxBwType,'extremeIQosProfileMaxBw':extremeIQosProfileMaxBw,'extremeIQosProfileRED':extremeIQosProfileRED,'extremeIQosProfileMaxBuf':extremeIQosProfileMaxBuf,'extremeIQosByVlanMappingTable':extremeIQosByVlanMappingTable,'extremeIQosByVlanMappingEntry':extremeIQosByVlanMappingEntry,'extremeIQosByVlanMappingIQosProfileIndex':extremeIQosByVlanMappingIQosProfileIndex})