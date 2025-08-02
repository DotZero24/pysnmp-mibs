_A7='juniSonetPathNotificationGroup'
_A6='juniSonetPathGroup3'
_A5='juniSonetPathGroup2'
_A4='juniSonetGroup2'
_A3='juniSonetVirtualTributaryGroup'
_A2='juniSonetPathEvents'
_A1='juniSonetMediumTriggerDelay'
_A0='juniSonetMediumTriggerAlarms'
_z='juniSonetVTIfIndex'
_y='accessible-for-notify'
_x='JuniSonetPathC2ByteOverride'
_w='not-accessible'
_v='juniSonetPathIfIndex'
_u='TruthValue'
_t='Unsigned32'
_s='ifAlias'
_r='juniSonetGroup3'
_q='juniSonetPathGroup'
_p='juniSonetGroup'
_o='juniSonetPathEventStatus'
_n='juniSonetPathEventIfIndex'
_m='juniSonetPathTriggerDelay'
_l='juniSonetPathC2ByteOverride'
_k='juniSonetPathC2ByteOverrideFlag'
_j='juniSonetPathTriggerAlarms'
_i='juniSonetVTRowStatus'
_h='juniSonetVTLowerIfIndex'
_g='juniSonetVTTributarySubChannel'
_f='juniSonetVTTributaryGroup'
_e='juniSonetVTPathPayload'
_d='juniSonetVTType'
_c='juniSonetVTPathLogicalChannel'
_b='juniSonetVTNextIfIndex'
_a='juniSonetMediumCircuitIdentifier'
_Z='juniSonetMediumType'
_Y='Bits'
_X='ifIndex'
_W='juniSonetVirtualTributaryGroup2'
_V='juniSonetPathRowStatus'
_U='juniSonetPathLowerIfIndex'
_T='juniSonetPathHierarchy'
_S='juniSonetPathSpeed'
_R='juniSonetPathLogicalChannel'
_Q='juniSonetPathNextIfIndex'
_P='juniSonetPathMaximumPathSpeed'
_O='juniSonetPathMinimumPathSpeed'
_N='juniSonetPathMaximumChannels'
_M='juniSonetPathChannelized'
_L='juniSonetPathRemoveFlag'
_K='juniSonetMediumTimingSource'
_J='juniSonetMediumLoopbackConfig'
_I='IF-MIB'
_H='read-write'
_G='deprecated'
_F='Integer32'
_E='read-only'
_D='obsolete'
_C='read-create'
_B='current'
_A='Juniper-UNI-SONET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifAlias,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex','InterfaceIndexOrZero',_s,_X)
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Y,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_t,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_u)
juniSonetMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,7))
if mibBuilder.loadTexts:juniSonetMIB.setRevisions(('2003-07-16 19:52','2002-11-22 16:37','2001-10-10 20:42','2001-01-02 18:00','1998-11-13 00:00'))
class JuniSonetLineSpeed(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('sonetUnknownSpeed',0),('sonetOc1Stm0',1),('sonetOc3Stm1',2),('sonetOc12Stm3',3),('sonetOc48Stm16',4)))
class JuniSonetLogicalPathChannel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JuniSonetPathHierarchy(TextualConvention,OctetString):status=_B;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class JuniSonetPathC2ByteOverride(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class JuniSonetVTType(TextualConvention,Integer32):status=_G;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,5)));namedValues=NamedValues(*(('tribVT15TU11',0),('tribVT20TU12',1),('tribVT3',3),('tribVT6',4),('tribVT6c',5)))
_JuniSonetObjects_ObjectIdentity=ObjectIdentity
juniSonetObjects=_JuniSonetObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,1))
_JuniSonetMediumTable_Object=MibTable
juniSonetMediumTable=_JuniSonetMediumTable_Object((1,3,6,1,4,1,4874,2,2,7,1,1))
if mibBuilder.loadTexts:juniSonetMediumTable.setStatus(_B)
_JuniSonetMediumEntry_Object=MibTableRow
juniSonetMediumEntry=_JuniSonetMediumEntry_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1))
juniSonetMediumEntry.setIndexNames((0,_I,_X))
if mibBuilder.loadTexts:juniSonetMediumEntry.setStatus(_B)
class _JuniSonetMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_JuniSonetMediumType_Type.__name__=_F
_JuniSonetMediumType_Object=MibTableColumn
juniSonetMediumType=_JuniSonetMediumType_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,1),_JuniSonetMediumType_Type())
juniSonetMediumType.setMaxAccess(_H)
if mibBuilder.loadTexts:juniSonetMediumType.setStatus(_G)
class _JuniSonetMediumLoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sonetNoLoop',0),('sonetFacilityLoop',1),('sonetTerminalLoop',2),('sonetOtherLoop',3)))
_JuniSonetMediumLoopbackConfig_Type.__name__=_F
_JuniSonetMediumLoopbackConfig_Object=MibTableColumn
juniSonetMediumLoopbackConfig=_JuniSonetMediumLoopbackConfig_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,2),_JuniSonetMediumLoopbackConfig_Type())
juniSonetMediumLoopbackConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:juniSonetMediumLoopbackConfig.setStatus(_B)
class _JuniSonetMediumTimingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('loop',0),('internalModule',1),('internalChassis',2)))
_JuniSonetMediumTimingSource_Type.__name__=_F
_JuniSonetMediumTimingSource_Object=MibTableColumn
juniSonetMediumTimingSource=_JuniSonetMediumTimingSource_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,3),_JuniSonetMediumTimingSource_Type())
juniSonetMediumTimingSource.setMaxAccess(_H)
if mibBuilder.loadTexts:juniSonetMediumTimingSource.setStatus(_B)
_JuniSonetMediumCircuitIdentifier_Type=DisplayString
_JuniSonetMediumCircuitIdentifier_Object=MibTableColumn
juniSonetMediumCircuitIdentifier=_JuniSonetMediumCircuitIdentifier_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,4),_JuniSonetMediumCircuitIdentifier_Type())
juniSonetMediumCircuitIdentifier.setMaxAccess(_H)
if mibBuilder.loadTexts:juniSonetMediumCircuitIdentifier.setStatus(_G)
class _JuniSonetMediumTriggerAlarms_Type(Bits):defaultBinValue='1011';namedValues=NamedValues(*(('sectionLOS',0),('sectionLOF',1),('lineAIS',2),('lineRDI',3)))
_JuniSonetMediumTriggerAlarms_Type.__name__=_Y
_JuniSonetMediumTriggerAlarms_Object=MibTableColumn
juniSonetMediumTriggerAlarms=_JuniSonetMediumTriggerAlarms_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,5),_JuniSonetMediumTriggerAlarms_Type())
juniSonetMediumTriggerAlarms.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetMediumTriggerAlarms.setStatus(_B)
class _JuniSonetMediumTriggerDelay_Type(Integer32):defaultValue=2500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_JuniSonetMediumTriggerDelay_Type.__name__=_F
_JuniSonetMediumTriggerDelay_Object=MibTableColumn
juniSonetMediumTriggerDelay=_JuniSonetMediumTriggerDelay_Object((1,3,6,1,4,1,4874,2,2,7,1,1,1,6),_JuniSonetMediumTriggerDelay_Type())
juniSonetMediumTriggerDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:juniSonetMediumTriggerDelay.setStatus(_B)
if mibBuilder.loadTexts:juniSonetMediumTriggerDelay.setUnits('ms')
_JuniSonetPathObjects_ObjectIdentity=ObjectIdentity
juniSonetPathObjects=_JuniSonetPathObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,2))
_JuniSonetPathCapabilityTable_Object=MibTable
juniSonetPathCapabilityTable=_JuniSonetPathCapabilityTable_Object((1,3,6,1,4,1,4874,2,2,7,2,1))
if mibBuilder.loadTexts:juniSonetPathCapabilityTable.setStatus(_B)
_JuniSonetPathCapabilityEntry_Object=MibTableRow
juniSonetPathCapabilityEntry=_JuniSonetPathCapabilityEntry_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1))
juniSonetPathCapabilityEntry.setIndexNames((0,_I,_X))
if mibBuilder.loadTexts:juniSonetPathCapabilityEntry.setStatus(_B)
_JuniSonetPathRemoveFlag_Type=TruthValue
_JuniSonetPathRemoveFlag_Object=MibTableColumn
juniSonetPathRemoveFlag=_JuniSonetPathRemoveFlag_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1,1),_JuniSonetPathRemoveFlag_Type())
juniSonetPathRemoveFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathRemoveFlag.setStatus(_B)
_JuniSonetPathChannelized_Type=TruthValue
_JuniSonetPathChannelized_Object=MibTableColumn
juniSonetPathChannelized=_JuniSonetPathChannelized_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1,2),_JuniSonetPathChannelized_Type())
juniSonetPathChannelized.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathChannelized.setStatus(_B)
_JuniSonetPathMaximumChannels_Type=Unsigned32
_JuniSonetPathMaximumChannels_Object=MibTableColumn
juniSonetPathMaximumChannels=_JuniSonetPathMaximumChannels_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1,3),_JuniSonetPathMaximumChannels_Type())
juniSonetPathMaximumChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathMaximumChannels.setStatus(_B)
_JuniSonetPathMinimumPathSpeed_Type=JuniSonetLineSpeed
_JuniSonetPathMinimumPathSpeed_Object=MibTableColumn
juniSonetPathMinimumPathSpeed=_JuniSonetPathMinimumPathSpeed_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1,4),_JuniSonetPathMinimumPathSpeed_Type())
juniSonetPathMinimumPathSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathMinimumPathSpeed.setStatus(_B)
_JuniSonetPathMaximumPathSpeed_Type=JuniSonetLineSpeed
_JuniSonetPathMaximumPathSpeed_Object=MibTableColumn
juniSonetPathMaximumPathSpeed=_JuniSonetPathMaximumPathSpeed_Object((1,3,6,1,4,1,4874,2,2,7,2,1,1,5),_JuniSonetPathMaximumPathSpeed_Type())
juniSonetPathMaximumPathSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathMaximumPathSpeed.setStatus(_B)
_JuniSonetPathNextIfIndex_Type=JuniNextIfIndex
_JuniSonetPathNextIfIndex_Object=MibScalar
juniSonetPathNextIfIndex=_JuniSonetPathNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,2,2),_JuniSonetPathNextIfIndex_Type())
juniSonetPathNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetPathNextIfIndex.setStatus(_B)
_JuniSonetPathTable_Object=MibTable
juniSonetPathTable=_JuniSonetPathTable_Object((1,3,6,1,4,1,4874,2,2,7,2,3))
if mibBuilder.loadTexts:juniSonetPathTable.setStatus(_B)
_JuniSonetPathEntry_Object=MibTableRow
juniSonetPathEntry=_JuniSonetPathEntry_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1))
juniSonetPathEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:juniSonetPathEntry.setStatus(_B)
_JuniSonetPathIfIndex_Type=InterfaceIndex
_JuniSonetPathIfIndex_Object=MibTableColumn
juniSonetPathIfIndex=_JuniSonetPathIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,1),_JuniSonetPathIfIndex_Type())
juniSonetPathIfIndex.setMaxAccess(_w)
if mibBuilder.loadTexts:juniSonetPathIfIndex.setStatus(_B)
_JuniSonetPathLogicalChannel_Type=JuniSonetLogicalPathChannel
_JuniSonetPathLogicalChannel_Object=MibTableColumn
juniSonetPathLogicalChannel=_JuniSonetPathLogicalChannel_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,2),_JuniSonetPathLogicalChannel_Type())
juniSonetPathLogicalChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathLogicalChannel.setStatus(_B)
_JuniSonetPathSpeed_Type=JuniSonetLineSpeed
_JuniSonetPathSpeed_Object=MibTableColumn
juniSonetPathSpeed=_JuniSonetPathSpeed_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,3),_JuniSonetPathSpeed_Type())
juniSonetPathSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathSpeed.setStatus(_B)
_JuniSonetPathHierarchy_Type=JuniSonetPathHierarchy
_JuniSonetPathHierarchy_Object=MibTableColumn
juniSonetPathHierarchy=_JuniSonetPathHierarchy_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,4),_JuniSonetPathHierarchy_Type())
juniSonetPathHierarchy.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathHierarchy.setStatus(_B)
_JuniSonetPathLowerIfIndex_Type=InterfaceIndexOrZero
_JuniSonetPathLowerIfIndex_Object=MibTableColumn
juniSonetPathLowerIfIndex=_JuniSonetPathLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,5),_JuniSonetPathLowerIfIndex_Type())
juniSonetPathLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathLowerIfIndex.setStatus(_B)
_JuniSonetPathRowStatus_Type=RowStatus
_JuniSonetPathRowStatus_Object=MibTableColumn
juniSonetPathRowStatus=_JuniSonetPathRowStatus_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,6),_JuniSonetPathRowStatus_Type())
juniSonetPathRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathRowStatus.setStatus(_B)
class _JuniSonetPathTriggerAlarms_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*(('pathLOP',0),('pathAIS',1),('pathRDI',2)))
_JuniSonetPathTriggerAlarms_Type.__name__=_Y
_JuniSonetPathTriggerAlarms_Object=MibTableColumn
juniSonetPathTriggerAlarms=_JuniSonetPathTriggerAlarms_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,7),_JuniSonetPathTriggerAlarms_Type())
juniSonetPathTriggerAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathTriggerAlarms.setStatus(_B)
class _JuniSonetPathC2ByteOverrideFlag_Type(TruthValue):defaultValue=2
_JuniSonetPathC2ByteOverrideFlag_Type.__name__=_u
_JuniSonetPathC2ByteOverrideFlag_Object=MibTableColumn
juniSonetPathC2ByteOverrideFlag=_JuniSonetPathC2ByteOverrideFlag_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,8),_JuniSonetPathC2ByteOverrideFlag_Type())
juniSonetPathC2ByteOverrideFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathC2ByteOverrideFlag.setStatus(_B)
class _JuniSonetPathC2ByteOverride_Type(JuniSonetPathC2ByteOverride):defaultValue=0
_JuniSonetPathC2ByteOverride_Type.__name__=_x
_JuniSonetPathC2ByteOverride_Object=MibTableColumn
juniSonetPathC2ByteOverride=_JuniSonetPathC2ByteOverride_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,9),_JuniSonetPathC2ByteOverride_Type())
juniSonetPathC2ByteOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathC2ByteOverride.setStatus(_B)
class _JuniSonetPathTriggerDelay_Type(Integer32):defaultValue=2500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_JuniSonetPathTriggerDelay_Type.__name__=_F
_JuniSonetPathTriggerDelay_Object=MibTableColumn
juniSonetPathTriggerDelay=_JuniSonetPathTriggerDelay_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,10),_JuniSonetPathTriggerDelay_Type())
juniSonetPathTriggerDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetPathTriggerDelay.setStatus(_B)
if mibBuilder.loadTexts:juniSonetPathTriggerDelay.setUnits('ms')
class _JuniSonetPathEventStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_JuniSonetPathEventStatus_Type.__name__=_t
_JuniSonetPathEventStatus_Object=MibTableColumn
juniSonetPathEventStatus=_JuniSonetPathEventStatus_Object((1,3,6,1,4,1,4874,2,2,7,2,3,1,11),_JuniSonetPathEventStatus_Type())
juniSonetPathEventStatus.setMaxAccess(_y)
if mibBuilder.loadTexts:juniSonetPathEventStatus.setStatus(_B)
_JuniSonetVTObjects_ObjectIdentity=ObjectIdentity
juniSonetVTObjects=_JuniSonetVTObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,3))
_JuniSonetVTNextIfIndex_Type=JuniNextIfIndex
_JuniSonetVTNextIfIndex_Object=MibScalar
juniSonetVTNextIfIndex=_JuniSonetVTNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,3,1),_JuniSonetVTNextIfIndex_Type())
juniSonetVTNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSonetVTNextIfIndex.setStatus(_B)
_JuniSonetVTTable_Object=MibTable
juniSonetVTTable=_JuniSonetVTTable_Object((1,3,6,1,4,1,4874,2,2,7,3,2))
if mibBuilder.loadTexts:juniSonetVTTable.setStatus(_B)
_JuniSonetVTEntry_Object=MibTableRow
juniSonetVTEntry=_JuniSonetVTEntry_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1))
juniSonetVTEntry.setIndexNames((0,_A,_z))
if mibBuilder.loadTexts:juniSonetVTEntry.setStatus(_B)
_JuniSonetVTIfIndex_Type=InterfaceIndex
_JuniSonetVTIfIndex_Object=MibTableColumn
juniSonetVTIfIndex=_JuniSonetVTIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,1),_JuniSonetVTIfIndex_Type())
juniSonetVTIfIndex.setMaxAccess(_w)
if mibBuilder.loadTexts:juniSonetVTIfIndex.setStatus(_B)
_JuniSonetVTPathLogicalChannel_Type=JuniSonetLogicalPathChannel
_JuniSonetVTPathLogicalChannel_Object=MibTableColumn
juniSonetVTPathLogicalChannel=_JuniSonetVTPathLogicalChannel_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,2),_JuniSonetVTPathLogicalChannel_Type())
juniSonetVTPathLogicalChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTPathLogicalChannel.setStatus(_B)
_JuniSonetVTType_Type=JuniSonetVTType
_JuniSonetVTType_Object=MibTableColumn
juniSonetVTType=_JuniSonetVTType_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,3),_JuniSonetVTType_Type())
juniSonetVTType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTType.setStatus(_G)
_JuniSonetVTPathPayload_Type=Unsigned32
_JuniSonetVTPathPayload_Object=MibTableColumn
juniSonetVTPathPayload=_JuniSonetVTPathPayload_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,4),_JuniSonetVTPathPayload_Type())
juniSonetVTPathPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTPathPayload.setStatus(_B)
_JuniSonetVTTributaryGroup_Type=Unsigned32
_JuniSonetVTTributaryGroup_Object=MibTableColumn
juniSonetVTTributaryGroup=_JuniSonetVTTributaryGroup_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,5),_JuniSonetVTTributaryGroup_Type())
juniSonetVTTributaryGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTTributaryGroup.setStatus(_B)
_JuniSonetVTTributarySubChannel_Type=Unsigned32
_JuniSonetVTTributarySubChannel_Object=MibTableColumn
juniSonetVTTributarySubChannel=_JuniSonetVTTributarySubChannel_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,6),_JuniSonetVTTributarySubChannel_Type())
juniSonetVTTributarySubChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTTributarySubChannel.setStatus(_B)
_JuniSonetVTLowerIfIndex_Type=InterfaceIndexOrZero
_JuniSonetVTLowerIfIndex_Object=MibTableColumn
juniSonetVTLowerIfIndex=_JuniSonetVTLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,7),_JuniSonetVTLowerIfIndex_Type())
juniSonetVTLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTLowerIfIndex.setStatus(_B)
_JuniSonetVTRowStatus_Type=RowStatus
_JuniSonetVTRowStatus_Object=MibTableColumn
juniSonetVTRowStatus=_JuniSonetVTRowStatus_Object((1,3,6,1,4,1,4874,2,2,7,3,2,1,8),_JuniSonetVTRowStatus_Type())
juniSonetVTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSonetVTRowStatus.setStatus(_B)
_JuniSonetConformance_ObjectIdentity=ObjectIdentity
juniSonetConformance=_JuniSonetConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,4))
_JuniSonetCompliances_ObjectIdentity=ObjectIdentity
juniSonetCompliances=_JuniSonetCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,4,1))
_JuniSonetGroups_ObjectIdentity=ObjectIdentity
juniSonetGroups=_JuniSonetGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,4,2))
_JuniSonetTrapControl_ObjectIdentity=ObjectIdentity
juniSonetTrapControl=_JuniSonetTrapControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,5))
_JuniSonetPathEventIfIndex_Type=InterfaceIndex
_JuniSonetPathEventIfIndex_Object=MibScalar
juniSonetPathEventIfIndex=_JuniSonetPathEventIfIndex_Object((1,3,6,1,4,1,4874,2,2,7,5,1),_JuniSonetPathEventIfIndex_Type())
juniSonetPathEventIfIndex.setMaxAccess(_y)
if mibBuilder.loadTexts:juniSonetPathEventIfIndex.setStatus(_B)
_JuniSonetTraps_ObjectIdentity=ObjectIdentity
juniSonetTraps=_JuniSonetTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,6))
_JuniSonetTrapPrefix_ObjectIdentity=ObjectIdentity
juniSonetTrapPrefix=_JuniSonetTrapPrefix_ObjectIdentity((1,3,6,1,4,1,4874,2,2,7,6,0))
juniSonetGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,1))
juniSonetGroup.setObjects(*((_A,_Z),(_A,_J),(_A,_K),(_A,_a)))
if mibBuilder.loadTexts:juniSonetGroup.setStatus(_D)
juniSonetPathGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,2))
juniSonetPathGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:juniSonetPathGroup.setStatus(_D)
juniSonetVirtualTributaryGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,3))
juniSonetVirtualTributaryGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:juniSonetVirtualTributaryGroup.setStatus(_D)
juniSonetGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,4))
juniSonetGroup2.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniSonetGroup2.setStatus(_D)
juniSonetVirtualTributaryGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,5))
juniSonetVirtualTributaryGroup2.setObjects(*((_A,_b),(_A,_c),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:juniSonetVirtualTributaryGroup2.setStatus(_B)
juniSonetDeprecatedMediumGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,6))
juniSonetDeprecatedMediumGroup.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:juniSonetDeprecatedMediumGroup.setStatus(_G)
juniSonetDeprecatedVTGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,7))
juniSonetDeprecatedVTGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:juniSonetDeprecatedVTGroup.setStatus(_G)
juniSonetGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,8))
juniSonetGroup3.setObjects(*((_A,_J),(_A,_K),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:juniSonetGroup3.setStatus(_B)
juniSonetPathGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,9))
juniSonetPathGroup2.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:juniSonetPathGroup2.setStatus(_D)
juniSonetPathGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,7,4,2,10))
juniSonetPathGroup3.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:juniSonetPathGroup3.setStatus(_B)
juniSonetPathEvents=NotificationType((1,3,6,1,4,1,4874,2,2,7,6,0,1))
juniSonetPathEvents.setObjects(*((_A,_n),(_A,_o),(_I,_s)))
if mibBuilder.loadTexts:juniSonetPathEvents.setStatus(_B)
juniSonetPathNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,7,4,2,11))
juniSonetPathNotificationGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:juniSonetPathNotificationGroup.setStatus(_B)
juniSonetCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,7,4,1,1))
juniSonetCompliance.setObjects((_A,_p))
if mibBuilder.loadTexts:juniSonetCompliance.setStatus(_D)
juniSonetCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,7,4,1,2))
juniSonetCompliance2.setObjects(*((_A,_p),(_A,_q),(_A,_A3)))
if mibBuilder.loadTexts:juniSonetCompliance2.setStatus(_D)
juniSonetCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,7,4,1,3))
juniSonetCompliance3.setObjects(*((_A,_A4),(_A,_q),(_A,_W)))
if mibBuilder.loadTexts:juniSonetCompliance3.setStatus(_D)
juniSonetCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,7,4,1,4))
juniSonetCompliance4.setObjects(*((_A,_r),(_A,_A5),(_A,_W)))
if mibBuilder.loadTexts:juniSonetCompliance4.setStatus(_D)
juniSonetCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,7,4,1,5))
juniSonetCompliance5.setObjects(*((_A,_r),(_A,_A6),(_A,_A7),(_A,_W)))
if mibBuilder.loadTexts:juniSonetCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniSonetLineSpeed':JuniSonetLineSpeed,'JuniSonetLogicalPathChannel':JuniSonetLogicalPathChannel,'JuniSonetPathHierarchy':JuniSonetPathHierarchy,_x:JuniSonetPathC2ByteOverride,'JuniSonetVTType':JuniSonetVTType,'juniSonetMIB':juniSonetMIB,'juniSonetObjects':juniSonetObjects,'juniSonetMediumTable':juniSonetMediumTable,'juniSonetMediumEntry':juniSonetMediumEntry,_Z:juniSonetMediumType,_J:juniSonetMediumLoopbackConfig,_K:juniSonetMediumTimingSource,_a:juniSonetMediumCircuitIdentifier,_A0:juniSonetMediumTriggerAlarms,_A1:juniSonetMediumTriggerDelay,'juniSonetPathObjects':juniSonetPathObjects,'juniSonetPathCapabilityTable':juniSonetPathCapabilityTable,'juniSonetPathCapabilityEntry':juniSonetPathCapabilityEntry,_L:juniSonetPathRemoveFlag,_M:juniSonetPathChannelized,_N:juniSonetPathMaximumChannels,_O:juniSonetPathMinimumPathSpeed,_P:juniSonetPathMaximumPathSpeed,_Q:juniSonetPathNextIfIndex,'juniSonetPathTable':juniSonetPathTable,'juniSonetPathEntry':juniSonetPathEntry,_v:juniSonetPathIfIndex,_R:juniSonetPathLogicalChannel,_S:juniSonetPathSpeed,_T:juniSonetPathHierarchy,_U:juniSonetPathLowerIfIndex,_V:juniSonetPathRowStatus,_j:juniSonetPathTriggerAlarms,_k:juniSonetPathC2ByteOverrideFlag,_l:juniSonetPathC2ByteOverride,_m:juniSonetPathTriggerDelay,_o:juniSonetPathEventStatus,'juniSonetVTObjects':juniSonetVTObjects,_b:juniSonetVTNextIfIndex,'juniSonetVTTable':juniSonetVTTable,'juniSonetVTEntry':juniSonetVTEntry,_z:juniSonetVTIfIndex,_c:juniSonetVTPathLogicalChannel,_d:juniSonetVTType,_e:juniSonetVTPathPayload,_f:juniSonetVTTributaryGroup,_g:juniSonetVTTributarySubChannel,_h:juniSonetVTLowerIfIndex,_i:juniSonetVTRowStatus,'juniSonetConformance':juniSonetConformance,'juniSonetCompliances':juniSonetCompliances,'juniSonetCompliance':juniSonetCompliance,'juniSonetCompliance2':juniSonetCompliance2,'juniSonetCompliance3':juniSonetCompliance3,'juniSonetCompliance4':juniSonetCompliance4,'juniSonetCompliance5':juniSonetCompliance5,'juniSonetGroups':juniSonetGroups,_p:juniSonetGroup,_q:juniSonetPathGroup,_A3:juniSonetVirtualTributaryGroup,_A4:juniSonetGroup2,_W:juniSonetVirtualTributaryGroup2,'juniSonetDeprecatedMediumGroup':juniSonetDeprecatedMediumGroup,'juniSonetDeprecatedVTGroup':juniSonetDeprecatedVTGroup,_r:juniSonetGroup3,_A5:juniSonetPathGroup2,_A6:juniSonetPathGroup3,_A7:juniSonetPathNotificationGroup,'juniSonetTrapControl':juniSonetTrapControl,_n:juniSonetPathEventIfIndex,'juniSonetTraps':juniSonetTraps,'juniSonetTrapPrefix':juniSonetTrapPrefix,_A2:juniSonetPathEvents})