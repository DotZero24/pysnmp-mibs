_R='ntcRedunConfGrpV1Standard'
_Q='ntcRedunOpState'
_P='ntcRedunCarrName'
_O='ntcRedunCarrType'
_N='ntcRedunType'
_M='ntcRedunOperationalState'
_L='ntcRedunInitialState'
_K='ntcRedunEnable'
_J='ntcRedunMonitoringName'
_I='NtcEnable'
_H='active'
_G='standby'
_F='read-write'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='NEWTEC-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ntcRedundancy=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1800))
if mibBuilder.loadTexts:ntcRedundancy.setRevisions(('2018-01-16 10:00','2013-01-08 12:00','2012-06-28 12:00'))
_NtcRedunObjects_ObjectIdentity=ObjectIdentity
ntcRedunObjects=_NtcRedunObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1800,1))
if mibBuilder.loadTexts:ntcRedunObjects.setStatus(_A)
class _NtcRedunEnable_Type(NtcEnable):defaultValue=0
_NtcRedunEnable_Type.__name__=_I
_NtcRedunEnable_Object=MibScalar
ntcRedunEnable=_NtcRedunEnable_Object((1,3,6,1,4,1,5835,5,2,1800,1,1),_NtcRedunEnable_Type())
ntcRedunEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcRedunEnable.setStatus(_A)
class _NtcRedunInitialState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NtcRedunInitialState_Type.__name__=_C
_NtcRedunInitialState_Object=MibScalar
ntcRedunInitialState=_NtcRedunInitialState_Object((1,3,6,1,4,1,5835,5,2,1800,1,2),_NtcRedunInitialState_Type())
ntcRedunInitialState.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcRedunInitialState.setStatus(_A)
class _NtcRedunOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_G,1),('na',2)))
_NtcRedunOperationalState_Type.__name__=_C
_NtcRedunOperationalState_Object=MibScalar
ntcRedunOperationalState=_NtcRedunOperationalState_Object((1,3,6,1,4,1,5835,5,2,1800,1,3),_NtcRedunOperationalState_Type())
ntcRedunOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRedunOperationalState.setStatus(_A)
class _NtcRedunType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unit',0),('carrier',1)))
_NtcRedunType_Type.__name__=_C
_NtcRedunType_Object=MibScalar
ntcRedunType=_NtcRedunType_Object((1,3,6,1,4,1,5835,5,2,1800,1,4),_NtcRedunType_Type())
ntcRedunType.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcRedunType.setStatus(_A)
_NtcRedunMonitoringTable_Object=MibTable
ntcRedunMonitoringTable=_NtcRedunMonitoringTable_Object((1,3,6,1,4,1,5835,5,2,1800,1,5))
if mibBuilder.loadTexts:ntcRedunMonitoringTable.setStatus(_A)
_NtcRedunMonitoringEntry_Object=MibTableRow
ntcRedunMonitoringEntry=_NtcRedunMonitoringEntry_Object((1,3,6,1,4,1,5835,5,2,1800,1,5,1))
ntcRedunMonitoringEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcRedunMonitoringEntry.setStatus(_A)
_NtcRedunMonitoringName_Type=Unsigned32
_NtcRedunMonitoringName_Object=MibTableColumn
ntcRedunMonitoringName=_NtcRedunMonitoringName_Object((1,3,6,1,4,1,5835,5,2,1800,1,5,1,1),_NtcRedunMonitoringName_Type())
ntcRedunMonitoringName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcRedunMonitoringName.setStatus(_A)
class _NtcRedunCarrType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcRedunCarrType_Type.__name__=_E
_NtcRedunCarrType_Object=MibTableColumn
ntcRedunCarrType=_NtcRedunCarrType_Object((1,3,6,1,4,1,5835,5,2,1800,1,5,1,2),_NtcRedunCarrType_Type())
ntcRedunCarrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRedunCarrType.setStatus(_A)
class _NtcRedunCarrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcRedunCarrName_Type.__name__=_E
_NtcRedunCarrName_Object=MibTableColumn
ntcRedunCarrName=_NtcRedunCarrName_Object((1,3,6,1,4,1,5835,5,2,1800,1,5,1,3),_NtcRedunCarrName_Type())
ntcRedunCarrName.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRedunCarrName.setStatus(_A)
class _NtcRedunOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_G,1),('na',2)))
_NtcRedunOpState_Type.__name__=_C
_NtcRedunOpState_Object=MibTableColumn
ntcRedunOpState=_NtcRedunOpState_Object((1,3,6,1,4,1,5835,5,2,1800,1,5,1,4),_NtcRedunOpState_Type())
ntcRedunOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRedunOpState.setStatus(_A)
_NtcRedunConformance_ObjectIdentity=ObjectIdentity
ntcRedunConformance=_NtcRedunConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1800,2))
if mibBuilder.loadTexts:ntcRedunConformance.setStatus(_A)
_NtcRedunConfCompliance_ObjectIdentity=ObjectIdentity
ntcRedunConfCompliance=_NtcRedunConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1800,2,1))
if mibBuilder.loadTexts:ntcRedunConfCompliance.setStatus(_A)
_NtcRedunConfGroup_ObjectIdentity=ObjectIdentity
ntcRedunConfGroup=_NtcRedunConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1800,2,2))
if mibBuilder.loadTexts:ntcRedunConfGroup.setStatus(_A)
ntcRedunConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1800,2,2,1))
ntcRedunConfGrpV1Standard.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ntcRedunConfGrpV1Standard.setStatus(_A)
ntcRedunConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1800,2,1,1))
ntcRedunConfCompV1Standard.setObjects((_B,_R))
if mibBuilder.loadTexts:ntcRedunConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcRedundancy':ntcRedundancy,'ntcRedunObjects':ntcRedunObjects,_K:ntcRedunEnable,_L:ntcRedunInitialState,_M:ntcRedunOperationalState,_N:ntcRedunType,'ntcRedunMonitoringTable':ntcRedunMonitoringTable,'ntcRedunMonitoringEntry':ntcRedunMonitoringEntry,_J:ntcRedunMonitoringName,_O:ntcRedunCarrType,_P:ntcRedunCarrName,_Q:ntcRedunOpState,'ntcRedunConformance':ntcRedunConformance,'ntcRedunConfCompliance':ntcRedunConfCompliance,'ntcRedunConfCompV1Standard':ntcRedunConfCompV1Standard,'ntcRedunConfGroup':ntcRedunConfGroup,_R:ntcRedunConfGrpV1Standard})