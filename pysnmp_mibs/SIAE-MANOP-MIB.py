_G='read-write'
_F='manualOpId'
_E='SIAE-MANOP-MIB'
_D='AlarmSeverityCode'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_D,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
manualOperation=ModuleIdentity((1,3,6,1,4,1,3373,1103,71))
if mibBuilder.loadTexts:manualOperation.setRevisions(('2014-03-17 00:00','2014-02-03 00:00','2013-04-16 00:00'))
_ManualOpTrap_ObjectIdentity=ObjectIdentity
manualOpTrap=_ManualOpTrap_ObjectIdentity((1,3,6,1,4,1,3373,1103,71,0))
class _ManualOpMibVersion_Type(Integer32):defaultValue=1
_ManualOpMibVersion_Type.__name__=_C
_ManualOpMibVersion_Object=MibScalar
manualOpMibVersion=_ManualOpMibVersion_Object((1,3,6,1,4,1,3373,1103,71,1),_ManualOpMibVersion_Type())
manualOpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpMibVersion.setStatus(_A)
_ManualOpTable_Object=MibTable
manualOpTable=_ManualOpTable_Object((1,3,6,1,4,1,3373,1103,71,2))
if mibBuilder.loadTexts:manualOpTable.setStatus(_A)
_ManualOpRecord_Object=MibTableRow
manualOpRecord=_ManualOpRecord_Object((1,3,6,1,4,1,3373,1103,71,2,1))
manualOpRecord.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:manualOpRecord.setStatus(_A)
_ManualOpId_Type=Integer32
_ManualOpId_Object=MibTableColumn
manualOpId=_ManualOpId_Object((1,3,6,1,4,1,3373,1103,71,2,1,1),_ManualOpId_Type())
manualOpId.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpId.setStatus(_A)
_ManualOpObjectId_Type=ObjectIdentifier
_ManualOpObjectId_Object=MibTableColumn
manualOpObjectId=_ManualOpObjectId_Object((1,3,6,1,4,1,3373,1103,71,2,1,2),_ManualOpObjectId_Type())
manualOpObjectId.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpObjectId.setStatus(_A)
_ManualOpEventTime_Type=Unsigned32
_ManualOpEventTime_Object=MibTableColumn
manualOpEventTime=_ManualOpEventTime_Object((1,3,6,1,4,1,3373,1103,71,2,1,3),_ManualOpEventTime_Type())
manualOpEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpEventTime.setStatus(_A)
class _ManualOpValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('integer32',1),('objectId',2)))
_ManualOpValueType_Type.__name__=_C
_ManualOpValueType_Object=MibTableColumn
manualOpValueType=_ManualOpValueType_Object((1,3,6,1,4,1,3373,1103,71,2,1,4),_ManualOpValueType_Type())
manualOpValueType.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpValueType.setStatus(_A)
_ManualOpIntegerVal_Type=Integer32
_ManualOpIntegerVal_Object=MibTableColumn
manualOpIntegerVal=_ManualOpIntegerVal_Object((1,3,6,1,4,1,3373,1103,71,2,1,5),_ManualOpIntegerVal_Type())
manualOpIntegerVal.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpIntegerVal.setStatus(_A)
_ManualOpOidVal_Type=ObjectIdentifier
_ManualOpOidVal_Object=MibTableColumn
manualOpOidVal=_ManualOpOidVal_Object((1,3,6,1,4,1,3373,1103,71,2,1,6),_ManualOpOidVal_Type())
manualOpOidVal.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpOidVal.setStatus(_A)
_ManualOpActive_Type=AlarmStatus
_ManualOpActive_Object=MibScalar
manualOpActive=_ManualOpActive_Object((1,3,6,1,4,1,3373,1103,71,3),_ManualOpActive_Type())
manualOpActive.setMaxAccess(_B)
if mibBuilder.loadTexts:manualOpActive.setStatus(_A)
class _ManualOpActiveSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_ManualOpActiveSeverityCode_Type.__name__=_D
_ManualOpActiveSeverityCode_Object=MibScalar
manualOpActiveSeverityCode=_ManualOpActiveSeverityCode_Object((1,3,6,1,4,1,3373,1103,71,4),_ManualOpActiveSeverityCode_Type())
manualOpActiveSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:manualOpActiveSeverityCode.setStatus(_A)
class _ManualOpTimeOut_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,172800))
_ManualOpTimeOut_Type.__name__=_C
_ManualOpTimeOut_Object=MibScalar
manualOpTimeOut=_ManualOpTimeOut_Object((1,3,6,1,4,1,3373,1103,71,5),_ManualOpTimeOut_Type())
manualOpTimeOut.setMaxAccess(_G)
if mibBuilder.loadTexts:manualOpTimeOut.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'manualOperation':manualOperation,'manualOpTrap':manualOpTrap,'manualOpMibVersion':manualOpMibVersion,'manualOpTable':manualOpTable,'manualOpRecord':manualOpRecord,_F:manualOpId,'manualOpObjectId':manualOpObjectId,'manualOpEventTime':manualOpEventTime,'manualOpValueType':manualOpValueType,'manualOpIntegerVal':manualOpIntegerVal,'manualOpOidVal':manualOpOidVal,'manualOpActive':manualOpActive,'manualOpActiveSeverityCode':manualOpActiveSeverityCode,'manualOpTimeOut':manualOpTimeOut})