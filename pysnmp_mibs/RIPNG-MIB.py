_G='swRIPngIfName'
_F='RIPNG-MIB'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swRIPngMIB=ModuleIdentity((1,3,6,1,4,1,171,12,83))
class _SwRIPngGlobalState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwRIPngGlobalState_Type.__name__=_B
_SwRIPngGlobalState_Object=MibScalar
swRIPngGlobalState=_SwRIPngGlobalState_Object((1,3,6,1,4,1,171,12,83,1),_SwRIPngGlobalState_Type())
swRIPngGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngGlobalState.setStatus(_A)
class _SwRIPngMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-horizon',1),('split-horizon',2),('poison-reverse',3)))
_SwRIPngMethod_Type.__name__=_B
_SwRIPngMethod_Object=MibScalar
swRIPngMethod=_SwRIPngMethod_Object((1,3,6,1,4,1,171,12,83,2),_SwRIPngMethod_Type())
swRIPngMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngMethod.setStatus(_A)
class _SwRIPngUpdateTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65535))
_SwRIPngUpdateTime_Type.__name__=_B
_SwRIPngUpdateTime_Object=MibScalar
swRIPngUpdateTime=_SwRIPngUpdateTime_Object((1,3,6,1,4,1,171,12,83,3),_SwRIPngUpdateTime_Type())
swRIPngUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngUpdateTime.setStatus(_A)
class _SwRIPngExpireTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwRIPngExpireTime_Type.__name__=_B
_SwRIPngExpireTime_Object=MibScalar
swRIPngExpireTime=_SwRIPngExpireTime_Object((1,3,6,1,4,1,171,12,83,4),_SwRIPngExpireTime_Type())
swRIPngExpireTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngExpireTime.setStatus(_A)
class _SwRIPngGarbageCollectionTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwRIPngGarbageCollectionTime_Type.__name__=_B
_SwRIPngGarbageCollectionTime_Object=MibScalar
swRIPngGarbageCollectionTime=_SwRIPngGarbageCollectionTime_Object((1,3,6,1,4,1,171,12,83,5),_SwRIPngGarbageCollectionTime_Type())
swRIPngGarbageCollectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngGarbageCollectionTime.setStatus(_A)
_SwRIPngIfTable_Object=MibTable
swRIPngIfTable=_SwRIPngIfTable_Object((1,3,6,1,4,1,171,12,83,6))
if mibBuilder.loadTexts:swRIPngIfTable.setStatus(_A)
_SwRIPngIfEntry_Object=MibTableRow
swRIPngIfEntry=_SwRIPngIfEntry_Object((1,3,6,1,4,1,171,12,83,6,1))
swRIPngIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:swRIPngIfEntry.setStatus(_A)
_SwRIPngIfName_Type=DisplayString
_SwRIPngIfName_Object=MibTableColumn
swRIPngIfName=_SwRIPngIfName_Object((1,3,6,1,4,1,171,12,83,6,1,1),_SwRIPngIfName_Type())
swRIPngIfName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swRIPngIfName.setStatus(_A)
class _SwRIPngIfState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwRIPngIfState_Type.__name__=_B
_SwRIPngIfState_Object=MibTableColumn
swRIPngIfState=_SwRIPngIfState_Object((1,3,6,1,4,1,171,12,83,6,1,2),_SwRIPngIfState_Type())
swRIPngIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngIfState.setStatus(_A)
class _SwRIPngIfMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_SwRIPngIfMetric_Type.__name__=_B
_SwRIPngIfMetric_Object=MibTableColumn
swRIPngIfMetric=_SwRIPngIfMetric_Object((1,3,6,1,4,1,171,12,83,6,1,3),_SwRIPngIfMetric_Type())
swRIPngIfMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swRIPngIfMetric.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'swRIPngMIB':swRIPngMIB,'swRIPngGlobalState':swRIPngGlobalState,'swRIPngMethod':swRIPngMethod,'swRIPngUpdateTime':swRIPngUpdateTime,'swRIPngExpireTime':swRIPngExpireTime,'swRIPngGarbageCollectionTime':swRIPngGarbageCollectionTime,'swRIPngIfTable':swRIPngIfTable,'swRIPngIfEntry':swRIPngIfEntry,_G:swRIPngIfName,'swRIPngIfState':swRIPngIfState,'swRIPngIfMetric':swRIPngIfMetric})