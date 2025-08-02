_r='hpicfVrrpv3VrBfdIPAddr'
_q='hpicfVrrpv3TrackRowStatus'
_p='hpicfVrrpv3IPv6RouterVrIdErrors'
_o='hpicfVrrpv3IPv4RouterVrIdErrors'
_n='hpicfVrrpv3IPv6RouterVersionErrors'
_m='hpicfVrrpv3IPv4RouterVersionErrors'
_l='hpicfVrrpv3IPv6RouterChecksumErrors'
_k='hpicfVrrpv3IPv4RouterChecksumErrors'
_j='hpicfVrrpv3NotificationCntl'
_i='hpicfVrrpv3Nonstop'
_h='hpicfVrrpv3RemoveConfig'
_g='hpicfVrrpv3RespondToPing'
_f='hpicfVrrpv3VrNullAuthCompatibility'
_e='hpicfVrrpv3StatsNearFailovers'
_d='hpicfVrrpv3VrControl'
_c='hpicfVrrpv3VrPreemptDelayTime'
_b='hpicfVrrpv3VrRespondToPing'
_a='hpicfVrrpv3VrMode'
_Z='hpicfVrrpv3Version'
_Y='hpicfVrrpv3IPv6AdminStatus'
_X='hpicfVrrpv3IPv4AdminStatus'
_W='hpicfVrrpv3StatsEntry'
_V='hpicfVrrpv3OperationsEntry'
_U='not-accessible'
_T='hpicfVrrpv3VrTrackEntity'
_S='hpicfVrrpv3VrTrackType'
_R='vrrpv3OperationsVrId'
_Q='vrrpv3OperationsInetAddrType'
_P='Counter32'
_O='SnmpAdminString'
_N='ifIndex'
_M='IF-MIB'
_L='hpicfVrrpv3BfdGroup'
_K='hpicfVrrpv3TrackGroup'
_J='hpicfVrrpv3OperGroup'
_I='VRRPV3-MIB'
_H='read-write'
_G='read-only'
_F='Integer32'
_E='Counter64'
_D='read-create'
_C='TruthValue'
_B='HP-ICF-VRRPV3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_M,_N)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_P,_E,'Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
vrrpv3AssociatedIpAddrEntry,vrrpv3OperationsEntry,vrrpv3OperationsInetAddrType,vrrpv3OperationsVrId=mibBuilder.importSymbols(_I,'vrrpv3AssociatedIpAddrEntry','vrrpv3OperationsEntry',_Q,_R)
hpicfVrrpv3MIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90))
if mibBuilder.loadTexts:hpicfVrrpv3MIB.setRevisions(('2015-09-16 00:00','2012-11-21 00:00','2012-10-25 00:00'))
_HpicfVrrpv3Operations_ObjectIdentity=ObjectIdentity
hpicfVrrpv3Operations=_HpicfVrrpv3Operations_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90,1))
class _HpicfVrrpv3IPv4AdminStatus_Type(TruthValue):defaultValue=2
_HpicfVrrpv3IPv4AdminStatus_Type.__name__=_C
_HpicfVrrpv3IPv4AdminStatus_Object=MibScalar
hpicfVrrpv3IPv4AdminStatus=_HpicfVrrpv3IPv4AdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,1),_HpicfVrrpv3IPv4AdminStatus_Type())
hpicfVrrpv3IPv4AdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3IPv4AdminStatus.setStatus(_A)
class _HpicfVrrpv3IPv6AdminStatus_Type(TruthValue):defaultValue=2
_HpicfVrrpv3IPv6AdminStatus_Type.__name__=_C
_HpicfVrrpv3IPv6AdminStatus_Object=MibScalar
hpicfVrrpv3IPv6AdminStatus=_HpicfVrrpv3IPv6AdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,2),_HpicfVrrpv3IPv6AdminStatus_Type())
hpicfVrrpv3IPv6AdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3IPv6AdminStatus.setStatus(_A)
_HpicfVrrpv3OperationsTable_Object=MibTable
hpicfVrrpv3OperationsTable=_HpicfVrrpv3OperationsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3))
if mibBuilder.loadTexts:hpicfVrrpv3OperationsTable.setStatus(_A)
_HpicfVrrpv3OperationsEntry_Object=MibTableRow
hpicfVrrpv3OperationsEntry=_HpicfVrrpv3OperationsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1))
if mibBuilder.loadTexts:hpicfVrrpv3OperationsEntry.setStatus(_A)
class _HpicfVrrpv3VrMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('owner',1),('backup',2),('uninitialized',3)))
_HpicfVrrpv3VrMode_Type.__name__=_F
_HpicfVrrpv3VrMode_Object=MibTableColumn
hpicfVrrpv3VrMode=_HpicfVrrpv3VrMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,1),_HpicfVrrpv3VrMode_Type())
hpicfVrrpv3VrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrMode.setStatus(_A)
class _HpicfVrrpv3VrPreemptDelayTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_HpicfVrrpv3VrPreemptDelayTime_Type.__name__=_F
_HpicfVrrpv3VrPreemptDelayTime_Object=MibTableColumn
hpicfVrrpv3VrPreemptDelayTime=_HpicfVrrpv3VrPreemptDelayTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,2),_HpicfVrrpv3VrPreemptDelayTime_Type())
hpicfVrrpv3VrPreemptDelayTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrPreemptDelayTime.setStatus(_A)
class _HpicfVrrpv3VrControl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('failback',1),('failover',2),('failoverWithMonitoring',3),('invalid',4)))
_HpicfVrrpv3VrControl_Type.__name__=_F
_HpicfVrrpv3VrControl_Object=MibTableColumn
hpicfVrrpv3VrControl=_HpicfVrrpv3VrControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,3),_HpicfVrrpv3VrControl_Type())
hpicfVrrpv3VrControl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrControl.setStatus(_A)
class _HpicfVrrpv3VrRespondToPing_Type(TruthValue):defaultValue=1
_HpicfVrrpv3VrRespondToPing_Type.__name__=_C
_HpicfVrrpv3VrRespondToPing_Object=MibTableColumn
hpicfVrrpv3VrRespondToPing=_HpicfVrrpv3VrRespondToPing_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,4),_HpicfVrrpv3VrRespondToPing_Type())
hpicfVrrpv3VrRespondToPing.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrRespondToPing.setStatus(_A)
class _HpicfVrrpv3Version_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('v2',2),('v3',3)))
_HpicfVrrpv3Version_Type.__name__=_F
_HpicfVrrpv3Version_Object=MibTableColumn
hpicfVrrpv3Version=_HpicfVrrpv3Version_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,5),_HpicfVrrpv3Version_Type())
hpicfVrrpv3Version.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3Version.setStatus(_A)
class _HpicfVrrpv3VrNullAuthCompatibility_Type(TruthValue):defaultValue=2
_HpicfVrrpv3VrNullAuthCompatibility_Type.__name__=_C
_HpicfVrrpv3VrNullAuthCompatibility_Object=MibTableColumn
hpicfVrrpv3VrNullAuthCompatibility=_HpicfVrrpv3VrNullAuthCompatibility_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,6),_HpicfVrrpv3VrNullAuthCompatibility_Type())
hpicfVrrpv3VrNullAuthCompatibility.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrNullAuthCompatibility.setStatus(_A)
_HpicfVrrpv3VrBfdIPAddr_Type=InetAddress
_HpicfVrrpv3VrBfdIPAddr_Object=MibTableColumn
hpicfVrrpv3VrBfdIPAddr=_HpicfVrrpv3VrBfdIPAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,3,1,13),_HpicfVrrpv3VrBfdIPAddr_Type())
hpicfVrrpv3VrBfdIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3VrBfdIPAddr.setStatus(_A)
_HpicfVrrpv3TrackTable_Object=MibTable
hpicfVrrpv3TrackTable=_HpicfVrrpv3TrackTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,4))
if mibBuilder.loadTexts:hpicfVrrpv3TrackTable.setStatus(_A)
_HpicfVrrpv3TrackEntry_Object=MibTableRow
hpicfVrrpv3TrackEntry=_HpicfVrrpv3TrackEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,4,1))
hpicfVrrpv3TrackEntry.setIndexNames((0,_M,_N),(0,_I,_R),(0,_I,_Q),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:hpicfVrrpv3TrackEntry.setStatus(_A)
class _HpicfVrrpv3VrTrackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port',1),('trunk',2),('vlan',3)))
_HpicfVrrpv3VrTrackType_Type.__name__=_F
_HpicfVrrpv3VrTrackType_Object=MibTableColumn
hpicfVrrpv3VrTrackType=_HpicfVrrpv3VrTrackType_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,4,1,1),_HpicfVrrpv3VrTrackType_Type())
hpicfVrrpv3VrTrackType.setMaxAccess(_U)
if mibBuilder.loadTexts:hpicfVrrpv3VrTrackType.setStatus(_A)
class _HpicfVrrpv3VrTrackEntity_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpicfVrrpv3VrTrackEntity_Type.__name__=_O
_HpicfVrrpv3VrTrackEntity_Object=MibTableColumn
hpicfVrrpv3VrTrackEntity=_HpicfVrrpv3VrTrackEntity_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,4,1,2),_HpicfVrrpv3VrTrackEntity_Type())
hpicfVrrpv3VrTrackEntity.setMaxAccess(_U)
if mibBuilder.loadTexts:hpicfVrrpv3VrTrackEntity.setStatus(_A)
_HpicfVrrpv3TrackRowStatus_Type=RowStatus
_HpicfVrrpv3TrackRowStatus_Object=MibTableColumn
hpicfVrrpv3TrackRowStatus=_HpicfVrrpv3TrackRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,4,1,3),_HpicfVrrpv3TrackRowStatus_Type())
hpicfVrrpv3TrackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfVrrpv3TrackRowStatus.setStatus(_A)
_HpicfVrrpv3StatsTable_Object=MibTable
hpicfVrrpv3StatsTable=_HpicfVrrpv3StatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,5))
if mibBuilder.loadTexts:hpicfVrrpv3StatsTable.setStatus(_A)
_HpicfVrrpv3StatsEntry_Object=MibTableRow
hpicfVrrpv3StatsEntry=_HpicfVrrpv3StatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,5,1))
if mibBuilder.loadTexts:hpicfVrrpv3StatsEntry.setStatus(_A)
class _HpicfVrrpv3StatsNearFailovers_Type(Counter32):defaultValue=0
_HpicfVrrpv3StatsNearFailovers_Type.__name__=_P
_HpicfVrrpv3StatsNearFailovers_Object=MibTableColumn
hpicfVrrpv3StatsNearFailovers=_HpicfVrrpv3StatsNearFailovers_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,5,1,1),_HpicfVrrpv3StatsNearFailovers_Type())
hpicfVrrpv3StatsNearFailovers.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3StatsNearFailovers.setStatus(_A)
class _HpicfVrrpv3RespondToPing_Type(TruthValue):defaultValue=2
_HpicfVrrpv3RespondToPing_Type.__name__=_C
_HpicfVrrpv3RespondToPing_Object=MibScalar
hpicfVrrpv3RespondToPing=_HpicfVrrpv3RespondToPing_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,6),_HpicfVrrpv3RespondToPing_Type())
hpicfVrrpv3RespondToPing.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3RespondToPing.setStatus(_A)
class _HpicfVrrpv3RemoveConfig_Type(TruthValue):defaultValue=2
_HpicfVrrpv3RemoveConfig_Type.__name__=_C
_HpicfVrrpv3RemoveConfig_Object=MibScalar
hpicfVrrpv3RemoveConfig=_HpicfVrrpv3RemoveConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,7),_HpicfVrrpv3RemoveConfig_Type())
hpicfVrrpv3RemoveConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3RemoveConfig.setStatus(_A)
class _HpicfVrrpv3Nonstop_Type(TruthValue):defaultValue=2
_HpicfVrrpv3Nonstop_Type.__name__=_C
_HpicfVrrpv3Nonstop_Object=MibScalar
hpicfVrrpv3Nonstop=_HpicfVrrpv3Nonstop_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,8),_HpicfVrrpv3Nonstop_Type())
hpicfVrrpv3Nonstop.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3Nonstop.setStatus(_A)
class _HpicfVrrpv3NotificationCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfVrrpv3NotificationCntl_Type.__name__=_F
_HpicfVrrpv3NotificationCntl_Object=MibScalar
hpicfVrrpv3NotificationCntl=_HpicfVrrpv3NotificationCntl_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,9),_HpicfVrrpv3NotificationCntl_Type())
hpicfVrrpv3NotificationCntl.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVrrpv3NotificationCntl.setStatus(_A)
_HpicfVrrpv3ErrorObjects_ObjectIdentity=ObjectIdentity
hpicfVrrpv3ErrorObjects=_HpicfVrrpv3ErrorObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10))
class _HpicfVrrpv3IPv4RouterChecksumErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv4RouterChecksumErrors_Type.__name__=_E
_HpicfVrrpv3IPv4RouterChecksumErrors_Object=MibScalar
hpicfVrrpv3IPv4RouterChecksumErrors=_HpicfVrrpv3IPv4RouterChecksumErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,1),_HpicfVrrpv3IPv4RouterChecksumErrors_Type())
hpicfVrrpv3IPv4RouterChecksumErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv4RouterChecksumErrors.setStatus(_A)
class _HpicfVrrpv3IPv6RouterChecksumErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv6RouterChecksumErrors_Type.__name__=_E
_HpicfVrrpv3IPv6RouterChecksumErrors_Object=MibScalar
hpicfVrrpv3IPv6RouterChecksumErrors=_HpicfVrrpv3IPv6RouterChecksumErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,2),_HpicfVrrpv3IPv6RouterChecksumErrors_Type())
hpicfVrrpv3IPv6RouterChecksumErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv6RouterChecksumErrors.setStatus(_A)
class _HpicfVrrpv3IPv4RouterVersionErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv4RouterVersionErrors_Type.__name__=_E
_HpicfVrrpv3IPv4RouterVersionErrors_Object=MibScalar
hpicfVrrpv3IPv4RouterVersionErrors=_HpicfVrrpv3IPv4RouterVersionErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,3),_HpicfVrrpv3IPv4RouterVersionErrors_Type())
hpicfVrrpv3IPv4RouterVersionErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv4RouterVersionErrors.setStatus(_A)
class _HpicfVrrpv3IPv6RouterVersionErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv6RouterVersionErrors_Type.__name__=_E
_HpicfVrrpv3IPv6RouterVersionErrors_Object=MibScalar
hpicfVrrpv3IPv6RouterVersionErrors=_HpicfVrrpv3IPv6RouterVersionErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,4),_HpicfVrrpv3IPv6RouterVersionErrors_Type())
hpicfVrrpv3IPv6RouterVersionErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv6RouterVersionErrors.setStatus(_A)
class _HpicfVrrpv3IPv4RouterVrIdErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv4RouterVrIdErrors_Type.__name__=_E
_HpicfVrrpv3IPv4RouterVrIdErrors_Object=MibScalar
hpicfVrrpv3IPv4RouterVrIdErrors=_HpicfVrrpv3IPv4RouterVrIdErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,5),_HpicfVrrpv3IPv4RouterVrIdErrors_Type())
hpicfVrrpv3IPv4RouterVrIdErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv4RouterVrIdErrors.setStatus(_A)
class _HpicfVrrpv3IPv6RouterVrIdErrors_Type(Counter64):defaultValue=0
_HpicfVrrpv3IPv6RouterVrIdErrors_Type.__name__=_E
_HpicfVrrpv3IPv6RouterVrIdErrors_Object=MibScalar
hpicfVrrpv3IPv6RouterVrIdErrors=_HpicfVrrpv3IPv6RouterVrIdErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,90,1,10,6),_HpicfVrrpv3IPv6RouterVrIdErrors_Type())
hpicfVrrpv3IPv6RouterVrIdErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVrrpv3IPv6RouterVrIdErrors.setStatus(_A)
_HpicfVrrpv3Conformance_ObjectIdentity=ObjectIdentity
hpicfVrrpv3Conformance=_HpicfVrrpv3Conformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90,2))
_HpicfVrrpv3MIBCompliances_ObjectIdentity=ObjectIdentity
hpicfVrrpv3MIBCompliances=_HpicfVrrpv3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90,2,1))
_HpicfVrrpv3MIBGroups_ObjectIdentity=ObjectIdentity
hpicfVrrpv3MIBGroups=_HpicfVrrpv3MIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,90,2,2))
vrrpv3OperationsEntry.registerAugmentions((_B,_V))
hpicfVrrpv3OperationsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
vrrpv3OperationsEntry.registerAugmentions((_B,_W))
hpicfVrrpv3StatsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
hpicfVrrpv3OperGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,90,2,2,1))
hpicfVrrpv3OperGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:hpicfVrrpv3OperGroup.setStatus(_A)
hpicfVrrpv3TrackGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,90,2,2,2))
hpicfVrrpv3TrackGroup.setObjects((_B,_q))
if mibBuilder.loadTexts:hpicfVrrpv3TrackGroup.setStatus(_A)
hpicfVrrpv3BfdGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,90,2,2,3))
hpicfVrrpv3BfdGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:hpicfVrrpv3BfdGroup.setStatus(_A)
hpicfVrrpv3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,90,2,1,1))
hpicfVrrpv3MIBCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfVrrpv3MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfVrrpv3MIB':hpicfVrrpv3MIB,'hpicfVrrpv3Operations':hpicfVrrpv3Operations,_X:hpicfVrrpv3IPv4AdminStatus,_Y:hpicfVrrpv3IPv6AdminStatus,'hpicfVrrpv3OperationsTable':hpicfVrrpv3OperationsTable,_V:hpicfVrrpv3OperationsEntry,_a:hpicfVrrpv3VrMode,_c:hpicfVrrpv3VrPreemptDelayTime,_d:hpicfVrrpv3VrControl,_b:hpicfVrrpv3VrRespondToPing,_Z:hpicfVrrpv3Version,_f:hpicfVrrpv3VrNullAuthCompatibility,_r:hpicfVrrpv3VrBfdIPAddr,'hpicfVrrpv3TrackTable':hpicfVrrpv3TrackTable,'hpicfVrrpv3TrackEntry':hpicfVrrpv3TrackEntry,_S:hpicfVrrpv3VrTrackType,_T:hpicfVrrpv3VrTrackEntity,_q:hpicfVrrpv3TrackRowStatus,'hpicfVrrpv3StatsTable':hpicfVrrpv3StatsTable,_W:hpicfVrrpv3StatsEntry,_e:hpicfVrrpv3StatsNearFailovers,_g:hpicfVrrpv3RespondToPing,_h:hpicfVrrpv3RemoveConfig,_i:hpicfVrrpv3Nonstop,_j:hpicfVrrpv3NotificationCntl,'hpicfVrrpv3ErrorObjects':hpicfVrrpv3ErrorObjects,_k:hpicfVrrpv3IPv4RouterChecksumErrors,_l:hpicfVrrpv3IPv6RouterChecksumErrors,_m:hpicfVrrpv3IPv4RouterVersionErrors,_n:hpicfVrrpv3IPv6RouterVersionErrors,_o:hpicfVrrpv3IPv4RouterVrIdErrors,_p:hpicfVrrpv3IPv6RouterVrIdErrors,'hpicfVrrpv3Conformance':hpicfVrrpv3Conformance,'hpicfVrrpv3MIBCompliances':hpicfVrrpv3MIBCompliances,'hpicfVrrpv3MIBCompliance':hpicfVrrpv3MIBCompliance,'hpicfVrrpv3MIBGroups':hpicfVrrpv3MIBGroups,_J:hpicfVrrpv3OperGroup,_K:hpicfVrrpv3TrackGroup,_L:hpicfVrrpv3BfdGroup})